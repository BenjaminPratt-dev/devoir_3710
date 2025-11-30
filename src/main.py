#!/usr/bin/env python3
"""
Main entry point for the optimal query plan cost solution.
This file handles stdin/stdout for Gradescope autograder.
"""

import sys
from solution import solve


def main():
    """
    Read from stdin, process, and write to stdout.
    
    Reads pairs of lines (query and cardinalities) until EOF.
    """
    while True:
        try:
            # query_line = input()
            # cardinalities_line = input()
            query_line = 'R1(b,x,y, a), R2(b,c,z), R3(c,d,w)'
            cardinalities_line = 'R1=1000; R2=500; R3=800'
            solve(query_line, cardinalities_line)
            break
        except EOFError:
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
