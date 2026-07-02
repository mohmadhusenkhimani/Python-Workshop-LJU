"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Lists
Platform            : HackerRank
Topic               : List
Difficulty          : Easy
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

Initialize an empty list and perform the given commands.

Commands:

1. insert i e
2. print
3. remove e
4. append e
5. sort
6. pop
7. reverse

===============================================================
"""

# ============================================================
# Input
# ============================================================

numbers = []

n = int(input())

# ============================================================
# Logic
# ============================================================

for i in range(n):

    command = input().split()

    if command[0] == "append":
        numbers.append(int(command[1]))

    elif command[0] == "insert":
        numbers.insert(int(command[1]), int(command[2]))

    elif command[0] == "remove":
        numbers.remove(int(command[1]))

    elif command[0] == "sort":
        numbers.sort()

    elif command[0] == "pop":
        numbers.pop()

    elif command[0] == "reverse":
        numbers.reverse()

    elif command[0] == "print":
        print(numbers)