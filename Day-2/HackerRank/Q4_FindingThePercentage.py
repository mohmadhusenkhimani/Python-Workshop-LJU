"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Finding the Percentage
Platform            : HackerRank
Topic               : Dictionary
Difficulty          : Easy
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

The provided code reads a list of students and their marks
for three subjects.

Store the student records in a dictionary where:

Key   -> Student Name
Value -> List of Marks

After storing the data, read the query student's name,
calculate the average marks, and print the result rounded
to two decimal places.

Example:

Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Output:
56.00

===============================================================
"""

# ============================================================
# Input
# ============================================================

studentMarks = {}

n = int(input())

for i in range(n):

    data = input().split()

    name = data[0]

    marks = list(map(float, data[1:]))

    studentMarks[name] = marks

queryName = input()

# ============================================================
# Logic
# ============================================================

average = sum(studentMarks[queryName]) / len(studentMarks[queryName])

# ============================================================
# Output
# ============================================================

print(f"{average:.2f}")