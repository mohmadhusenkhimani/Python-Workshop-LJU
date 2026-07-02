"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : List Comprehensions
Platform            : HackerRank
Topic               : List Comprehension
Difficulty          : Easy
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

Let's learn about list comprehensions!

You are given three integers x, y, and z representing the
dimensions of a cuboid, along with an integer n.

Print a list of all possible coordinates (i, j, k) where:

0 <= i <= x
0 <= j <= y
0 <= k <= z

Exclude all coordinates where:

i + j + k == n

The output should be displayed as a list.

Example:

Input:
1
1
2
3

Output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
 [1, 0, 0], [1, 0, 1], [1, 1, 0]]

===============================================================
"""

# ============================================================
# Input
# ============================================================

x = int(input())
y = int(input())
z = int(input())
n = int(input())

# ============================================================
# Logic
# ============================================================

result = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n
]

# ============================================================
# Output
# ============================================================

print(result)