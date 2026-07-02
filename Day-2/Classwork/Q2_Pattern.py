"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Pattern Printing
Topic               : Nested Loop
Language            : Python 3
Course              : MCA
University          : LJU
Author              : Mohmadhusen Khimani
===============================================================
"""

print("Pattern 1")

for i in range(1,4):
    for j in range(1,i+1):
        print(j,end="")
    print()

print()

print("Pattern 2")

for i in range(1,4):
    for j in range(i):
        print(chr(65+j),end="")
    print()