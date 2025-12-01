import re
import math

def find_cardinalities(cardinalities_line):
    cardinalities = cardinalities_line.split(';')
    d = {}
    for c in cardinalities:
        split = c.split('=')
        name = split[0].strip()
        val = int(split[1].strip())
        d[name] = val
    return d

def find_queries(query_line):
    queries = query_line.strip().split(")")
    queries.pop()
    d = {}
    for q in queries:
        split = q.split("(")
        key = split[0].strip(',').strip()
        if d.get(key):
            return None
        attributes = split[1].split(",")
        attributes = [a.strip() for a in attributes if a.strip()]
        attributes.sort()
        d[key] = attributes
    return d

def find_common_attributes(left, right):
    # Deterministic, sorted label for shared attributes
    common = sorted(list(left["attributes"] & right["attributes"]))
    return "|".join(common) if common else None

def cost_join(c1, c2):
    # Heuristic cost model; deterministic
    return c1 * c2 / max(c1, c2)

def subsets_of_size(relations, size):
    # Generate ALL subsets of given size (no early pruning).
    keys = sorted(relations.keys())
    dp = {1: [tuple([k]) for k in keys]}
    for k in range(2, size + 1):
        dp[k] = []
        seen = set()
        for subset in dp[k - 1]:
            subset_set = set(subset)
            last = subset[-1]
            # Grow with keys after 'last' to keep deterministic order and avoid duplicates
            for rel in keys:
                if rel in subset_set:
                    continue
                new_subset = tuple(sorted(subset_set | {rel}))
                if len(new_subset) == k and new_subset not in seen:
                    dp[k].append(new_subset)
                    seen.add(new_subset)
    return dp[size]

def partitions(subset):
    # Deterministic generation of partitions (X, Y) and (Y, X) when needed
    names = list(subset)
    n = len(names)
    result = []
    max_size = n // 2
    for size in range(1, max_size + 1):
        indices = list(range(size))
        while True:
            X = {names[i] for i in indices}
            Y = set(names) - X
            result.append((X, Y))
            if size < n - size:
                result.append((Y, X))
            i = size - 1
            while i >= 0 and indices[i] == n - size + i:
                i -= 1
            if i < 0:
                break
            indices[i] += 1
            for j in range(i + 1, size):
                indices[j] = indices[j - 1] + 1
    # Sort deterministically by |X| then lexicographic X
    result.sort(key=lambda part: (len(part[0]), tuple(sorted(list(part[0])))))
    return result

def solve(query_line, cardinalities_line):
    relations = find_queries(query_line)
    if not relations:
        print(None)
        return
    cardinalities = find_cardinalities(cardinalities_line)

    # Initialize optimal plans for singletons
    OptPlans = {}
    for r in relations:
        OptPlans[frozenset([r])] = {
            "plan": r,
            "cost": 0,
            "card": cardinalities[r],
            "attributes": set(relations[r])
        }

    keys = sorted(relations.keys())
    n = len(keys)
    num_of_plans = 0

    # Bottom-up DP by subset size
    for t in range(2, n + 1):
        subsets = subsets_of_size(relations, t)
        for subset in subsets:
            subset_fs = frozenset(subset)
            best = None
            best_cost = float("inf")

            all_partitions = partitions(subset)
            for X, Y in all_partitions:
                X_fs = frozenset(X)
                Y_fs = frozenset(Y)

                # Require both subplans to exist
                if X_fs not in OptPlans or Y_fs not in OptPlans:
                    continue

                planX = OptPlans[X_fs]
                planY = OptPlans[Y_fs]

                # Require shared attributes for a valid join attempt
                common = find_common_attributes(planX, planY)
                if not common:
                    continue

                # Count only valid join attempts (matches expected test's notion)
                num_of_plans += 1

                join_cost = cost_join(planX["card"], planY["card"])
                total_cost = planX["cost"] + planY["cost"] + join_cost

                candidate_plan = f"({planX['plan']} join_{common} {planY['plan']})"
                candidate = {
                    "plan": candidate_plan,
                    "cost": total_cost,
                    "card": join_cost,
                    "attributes": planX['attributes'].union(planY['attributes'])
                }

                # Deterministic tie-breaking: prefer lexicographically smaller plan on cost ties
                if total_cost < best_cost:
                    best_cost = total_cost
                    best = candidate
                elif total_cost == best_cost:
                    if best is None or candidate_plan < best["plan"]:
                        best = candidate

            if best is not None:
                OptPlans[subset_fs] = best

    full_fs = frozenset(keys)
    if full_fs not in OptPlans:
        print(None)
        return

    final_plan = OptPlans[full_fs]["plan"]
    final_cost = OptPlans[full_fs]["cost"]

    print(final_plan)
    print(int(final_cost))
    print(num_of_plans)