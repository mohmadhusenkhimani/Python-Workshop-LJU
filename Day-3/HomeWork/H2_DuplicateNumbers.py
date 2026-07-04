"""
================================================================
                    Python Workshop - LJU
----------------------------------------------------------------
Program Name        : Duplicate Numbers
Topic               : List
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

Write a Python program to find duplicate numbers
from a List.

The program should:

1. Accept list elements from the user.
2. Find all duplicate numbers.
3. Display the duplicate numbers.
4. If no duplicates are found, display an appropriate message.

================================================================
"""

# // Create Empty List
numbers = []

# // Input Number of Elements
size = int(input("Enter Number of Elements : "))

# // Accept List Elements
for i in range(size):
    value = int(input("Enter Element : "))
    numbers.append(value)

# // Display Original List
print("\nOriginal List :", numbers)

# // Create Empty List for Duplicates
duplicates = []

# // Find Duplicate Numbers
for number in numbers:

    if numbers.count(number) > 1:

        if number not in duplicates:

            duplicates.append(number)

# // Display Result
if len(duplicates) > 0:

    print("\nDuplicate Numbers :", duplicates)

else:

    print("\nNo Duplicate Numbers Found.")
