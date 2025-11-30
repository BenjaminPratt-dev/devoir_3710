"""
Solution module for the assignment.
Replace the example functions below with your actual solution code.
"""

import re
import math

def cost_join(c1, c2):
    return c1*c2/max(c1, c2)

def get_relations(max_size, queries, cardinalities):
    relations = {}
    joined = {}
    # add initial relations
    for q in queries.keys():
        relations[q] = cardinalities[q]
    
    for i in range(1, max_size):
        joined = {}
        for rel1 in relations.keys():
            #check size to not join relations already joined
            if len(rel1.split('join')) < i:
                continue

            for rel2 in queries.keys():
                #buffers in case they need to be swapped
                left = rel1
                right = rel2
                
                #base cost if already done a join
                base_cost = 0

                #dont join relation to itself or if the relation has already been joined
                if left == right or right in left:
                    continue

                # sort left and right to be in correct order if two base relations
                if right < left and 'join' not in left:
                    x = right
                    right = left
                    left = x
                
                # find common attributes
                attribute = None

                #if joined, find all attributes and base cost
                left_attributes = []
                if 'join' in left:
                    split = left.split(' ')

                    for s in split:
                        if 'join' in s:
                            continue
                        s = s.strip('(')
                        s = s.strip(')')
                        left_attributes += queries[s]

                    #remove duplicates
                    left_attributes = list(set(left_attributes))
                    left_attributes.sort()

                    base_cost = relations[left]
                else:
                    left_attributes = queries[left]
                        

                #join based on attributes
                for a1 in left_attributes:
                    for a2 in queries[right]:
                        if a1 == a2:
                            attribute = a1 if attribute == None else attribute + '|' + a1
                
                # if no common attribute, skip to avoid cartsien product
                if not attribute:
                    continue

                key = "(" + left + " join_" + attribute + " " + right + ")"
                cost = base_cost + cost_join(relations[left], relations[right])

                #check if relation already exists
                if not relations.get(key) and not joined.get(key):
                    joined[key] = cost
        relations = relations | joined
    return relations

def find_cardinalities(cardinalities_line):
    card = cardinalities_line.split(';')
    dict = {}

    for c in card:
        split = c.split('=')

        dict[split[0].strip()] = int(split[1].strip())
    
    return dict

def find_queries(query_line):
    queries = query_line.strip().split(")")
    queries.pop()

    dict = {}

    for q in queries:
        split = q.split("(")

        key = split[0]
        key = key.strip(',')
        key = key.strip(' ')

        attributes = split[1].split(",")
        attributes.sort()
        dict[key] = attributes
    return dict

def solve(query_line, cardinalities_line):
    queries = find_queries(query_line)
    cards = find_cardinalities(cardinalities_line)
        
    n = len(queries.keys())
    optimal_plan = ""
    optimal_cost = -1
    num_of_plans = 0

    relations = get_relations(n, queries, cards)

    print(relations)
    for r in relations.keys():
        valid = True

        #make sure every relation is in the query
        for q in queries.keys():
            if q not in r:
                valid = False
                break
        #check    
        if valid:
            num_of_plans += 1
            cost = relations[r]
            if optimal_cost == -1 or cost < optimal_cost:
                optimal_plan = r
                optimal_cost = cost

    print(optimal_plan)
    print(optimal_cost)
    print(num_of_plans)
