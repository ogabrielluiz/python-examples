"""Convert a m-base Number to a n-base Number."""

import math

def fibonacciDP(ith):
    """compute nth Fibonacci using Dynamic Programming Bottom-up"""
    if ith == 1 or ith == 2:
        return 1
    a, b = 1, 1
    i = 2
    while i < ith:
        i += 1
        b, a = a+b, b
    return b

def main():
    """Print octal equivelents of decimal numbers."""  
    print( fibonacciDP(3) )  # = 2
    
if __name__ == '__main__':
    main()