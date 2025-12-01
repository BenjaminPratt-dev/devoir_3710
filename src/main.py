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
            query_line = 'Q0(x,y,z),Q1(x,a,b),Q2(y,c,d),Q3(z,e,f),Q4(a,g,h),Q5(b,i,j),Q6(c,k,l),Q7(d,m,n),Q8(e,o,p),Q9(f,q,r),Q10(g,s,t),Q11(i,u,v),Q12(k,w,aa),Q13(m,bb,cc)'
            cardinalities_line = "Q0=130;Q1=140;Q2=120;Q3=150;Q4=110;Q5=160;Q6=130;Q7=140;Q8=120;Q9=150;Q10=110;Q11=160;Q12=130;Q13=140"
            solve(query_line, cardinalities_line)
            break
        except EOFError:
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
