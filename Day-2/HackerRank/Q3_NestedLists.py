"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Nested Lists
Platform            : HackerRank
Topic               : Lists
Difficulty          : Easy
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

Given the names and grades for each student in a class, store
them in a nested list and print the name(s) of any student(s)
having the second lowest grade.

If there are multiple students with the same second lowest
grade, print their names in alphabetical order.

Example:

Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Output:
Berry
Harry

===============================================================
"""

# ============================================================
# Input
# ============================================================

students = []

n = int(input())

for i in range(n):

    name = input()
    score = float(input())

    students.append([name, score])

# ============================================================
# Logic
# ============================================================

scores = []

for student in students:
    scores.append(student[1])

scores = sorted(set(scores))

secondLowest = scores[1]

result = []

for student in students:

    if student[1] == secondLowest:
        result.append(student[0])

result.sort()

# ============================================================
# Output
# ============================================================

for name in result:
    print(name)