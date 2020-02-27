#!/usr/bin/env python
"""fibonacci.py

Find the numbers in the fibonacci series up to n,
to a max of 1000."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import sys

# hard limit for argument n
max_n = 1000

def main():
    try:
        n = (int)(sys.argv[1])
        if n > 1000:
            raise ValueError
        elif n < 1:
            raise ValueError
    except(ValueError, IndexError):
        print("Usage: fibonacci.py [n]")
        print("[n] = how many numbers of sequence to display, up to 1000")
        sys.exit(1)

    fib = [1]
    if n == 1:
        print(fib)
    else:
        fib.append(1)

        if n == 2:
            print(fib)
        else:
            for x in range(2, n+1):
                fib.append(fib[x-1] + fib[x-2])
            print(fib)

if __name__ == "__main__":
    main()
