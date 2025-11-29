"""
Solution module for the assignment.
Replace the example functions below with your actual solution code.
"""

import re
import math


def find_relations(query_line):
    q = query_line.split(",")
    queries = []
    print(queries)
    dict = {}
    for i in range(len(queries)):
        if('(' in q[i] and ')' in q[i+1]):
            queries.append(q[i] + q[i+1])
            i+=1
        else:
            return False

    for q in queries:
        split = q.split("(")

        key = split[0]
        print(key)
        split[1] = split[1][:-1]
        attributes = split[1].split(",")
        print(attributes)

        dict[key] = attributes
        print(dict)
    return dict

def solve(query_line, cardinalities_line):
    dict = find_relations(query_line)
    print(dict)

    """ Add your logic to solve the problem here. """
    """ Print answers as below"""    
    optimal_plan = "OptimalPlanExample"
    optimal_cost = 123.45
    num_of_plans = 10

    print(optimal_plan)
    print(optimal_cost)
    print(num_of_plans)
