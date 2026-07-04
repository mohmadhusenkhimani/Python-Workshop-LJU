"""
================================================================
                    Python Workshop - LJU
----------------------------------------------------------------
Program Name        : Second Largest Number Using List
Topic               : List
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

Write a Python program to find the Second Largest Number
from a List.

The program should:

1. Accept list elements from the user.
2. Find the largest and second largest numbers.
3. Display the second largest number.

================================================================
"""

# // Create Empty List
numbers = []

# // Input List Elements
size = int(input("Enter Number of Elements : "))

for i in range(size):
    value = int(input("Enter Element : "))
    numbers.append(value)

# // Remove Duplicate Elements
uniqueNumbers = list(set(numbers))

# // Sort List
uniqueNumbers.sort()

# // Display Second Largest Number
if len(uniqueNumbers) >= 2:
    print("\nSecond Largest Number :", uniqueNumbers[-2])
else:
    print("\nSecond Largest Number Not Found.")
