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
            query_line = input()
            cardinalities_line = input()
            solve(query_line, cardinalities_line)
        except EOFError:
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
