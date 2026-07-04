"""
================================================================
                    Python Workshop - LJU
----------------------------------------------------------------
Program Name        : Tuple
Topic               : Tuple
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

Tuples are used to store multiple items in a single variable.
Unlike Lists, Tuples are immutable (cannot be modified).

Write a Python program to demonstrate the commonly used
Tuple operations and methods.

The program should perform the following operations:

1. Create Tuple
2. Access Elements
3. Tuple Slicing
4. Count Element
5. Find Index
6. Find Length
7. Check Membership
8. Traverse Tuple
9. Tuple Packing
10. Tuple Unpacking

================================================================
"""

# // Create Tuple
numbers = tuple(map(int, input("Enter Tuple Elements : ").split()))

print("\nOriginal Tuple :", numbers)

print("\n========== TUPLE OPERATIONS ==========")

# // Access First Element
print("\nFirst Element :", numbers[0])

# // Access Last Element
print("Last Element :", numbers[-1])

# // Tuple Slicing
print("\nFirst Three Elements :", numbers[:3])
print("Last Three Elements :", numbers[-3:])
print("Middle Elements :", numbers[1:-1])

# // Count Method
value = int(input("\nEnter Element to Count : "))
print("Count :", numbers.count(value))

# // Index Method
value = int(input("\nEnter Element to Find Index : "))

if value in numbers:
    print("Index :", numbers.index(value))
else:
    print("Element Not Found")

# // Length
print("\nLength :", len(numbers))

# // Membership
value = int(input("\nEnter Element to Search : "))

if value in numbers:
    print(value, "is Present")
else:
    print(value, "is Not Present")

# // Traverse Tuple
print("\nTuple Elements :")

for item in numbers:
    print(item)

# // Tuple Packing
student = ("Mohmadhusen", 22, "MCA")
print("\nPacked Tuple :", student)

# // Tuple Unpacking
name, age, course = student

print("\nTuple Unpacking")
print("Name   :", name)
print("Age    :", age)
print("Course :", course)
