"""
===============================================================
                Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Print Function
Topic               : Basic Data Types (HackerRank)
Data Structure Used : None
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

The included code stub will read an integer n.

Without using any string methods, print the numbers
from 1 to n as a single line.

Example:

Input:
5

Output:
12345

===============================================================
"""

# Read value of n
n = int(input())

# Print numbers from 1 to n without spaces
for i in range(1, n + 1):
    print(i, end="")