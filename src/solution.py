import re
import math

def find_cardinalities(cardinalities_line):
    cardinalities = cardinalities_line.split(';')
    dict = {}
    for c in cardinalities:
        split = c.split('=')
        dict[split[0].strip()] = int(split[1].strip())
    return dict

def find_queries(query_line):
    queries = query_line.strip().split(")")
    queries.pop()
    dict = {}
    for q in queries:
        split = q.split("(")
        key = split[0].strip(',').strip()

        if dict.get(key):
            return None
        
        attributes = split[1].split(",")
        attributes.sort()
        dict[key] = attributes
    return dict

def is_joinable(subset, relations):
    attrs = {rel: set(relations[rel]) for rel in subset}
    for rel in subset:
        shared = False
        for other in subset:
            if rel == other:
                continue
            if attrs[rel] & attrs[other]:
                shared = True
                break
        if not shared:
            return False
    return True

def subsets_of_size(relations, size):
    keys = sorted(relations.keys())
    n = len(keys)
    dp = {1: [tuple([k]) for k in keys]}

    for k in range(2, size + 1):
        dp[k] = []
        for subset in dp[k - 1]:
            for rel in keys:
                if rel in subset:
                    continue
                new_subset = tuple(sorted(set(subset) | {rel}))
                if len(new_subset) == k and new_subset not in dp[k]:
                    if is_joinable(new_subset, relations):
                        dp[k].append(new_subset)
    return dp[size]

def partitions(subset):
    names = list(subset)
    n = len(names)
    result = []

    for size in range(1, n):
        indices = list(range(size))
        while True:
            X = {names[i] for i in reversed(indices)}
            Y = set(names) - X
            result.append((X, Y))

            for i in reversed(range(size)):
                if indices[i] == 0:
                    break
            else:
                break
            indices[i] -= 1
            for j in range(i + 1, size):
                indices[j] = indices[j - 1] + 1

    result.sort(key=lambda part: (len(part[0]), sorted(part[0])))
    return result


def cost_join(c1, c2):
    return c1 * c2 / max(c1, c2)

def find_common_attributes(left, right): 
    attribute = None 
    for a1 in left['attributes']: 
        for a2 in right['attributes']: 
            if a1 == a2: 
                attribute = a1 if attribute == None else attribute + '|' + a1 
    return attribute

def solve(query_line, cardinalities_line):
    relations = find_queries(query_line)
    if not relations:
        print(None)
        return
    
    cardinalities = find_cardinalities(cardinalities_line)

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

    for t in range(2, n + 1):
        subsets = subsets_of_size(relations, t)
        for subset in subsets:
            subset_fs = frozenset(subset)
            best = None
            best_cost = float("inf")

            all_partitions = partitions(subset)
            for X, Y in all_partitions:
                num_of_plans += 1

                X_fs = frozenset(X)
                Y_fs = frozenset(Y)

                if X_fs not in OptPlans or Y_fs not in OptPlans:
                    continue

                planX = OptPlans[X_fs]
                planY = OptPlans[Y_fs]

                join_cost = cost_join(planX["card"], planY["card"])
                total_cost = planX["cost"] + planY["cost"] + join_cost


                if total_cost < best_cost:
                    best_cost = total_cost
                    best = {
                        "plan": f"({planX['plan']} join_{find_common_attributes(planX, planY)} {planY['plan']})",
                        "cost": total_cost,
                        "card": join_cost,
                        "attributes": planX['attributes'].union(planY['attributes'])
                    }

            if best is not None:
                OptPlans[subset_fs] = best

    full_fs = frozenset(keys)
    if full_fs in OptPlans:
        final_plan = OptPlans[full_fs]["plan"]
        final_cost = OptPlans[full_fs]["cost"]
    else:
        print(None)

    print(final_plan)
    print(int(final_cost))
    print(num_of_plans)
