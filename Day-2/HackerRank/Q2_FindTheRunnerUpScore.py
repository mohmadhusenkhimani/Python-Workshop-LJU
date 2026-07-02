"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Find the Runner-Up Score!
Platform            : HackerRank
Topic               : Lists
Difficulty          : Easy
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

Given the participants' score sheet for your University Sports Day,
find the runner-up score.

You are given n scores. Store them in a list and find the score of
the runner-up (second highest score).

Note:
If the highest score appears multiple times, remove all occurrences
before finding the runner-up score.

Example:

Input:
5
2 3 6 6 5

Output:
5

===============================================================
"""

# ============================================================
# Input
# ============================================================

n = int(input())

scores = list(map(int, input().split()))

# ============================================================
# Logic
# ============================================================

scores = list(set(scores))

scores.sort()

# ============================================================
# Output
# ============================================================

print(scores[-2])