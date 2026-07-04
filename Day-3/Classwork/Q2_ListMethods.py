"""
================================================================
                    Python Workshop - LJU
----------------------------------------------------------------
Program Name        : List Methods
Topic               : List
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

Lists are one of the most useful data structures in Python.

Write a Python program to demonstrate the commonly used
List methods.

The program should perform the following operations:

1. Append Element
2. Extend List
3. Insert Element
4. Remove Element
5. Pop Element
6. Sort List
7. Reverse List
8. Count Element
9. Find Index
10. Copy List
11. Clear List
12. Display List Length

================================================================
"""

# // Create Empty List
numbers = []

# // Enter Elements
size = int(input("How Many Elements : "))

for i in range(size):
    value = int(input("Enter Element : "))
    numbers.append(value)

print("\nOriginal List :", numbers)

print("\n========== LIST METHODS ==========")

# // Append
value = int(input("\nEnter Element to Append : "))
numbers.append(value)
print("After Append :", numbers)

# // Extend
extra = list(map(int, input("\nEnter Elements to Extend : ").split()))
numbers.extend(extra)
print("After Extend :", numbers)

# // Insert
position = int(input("\nEnter Position : "))
value = int(input("Enter Element : "))
numbers.insert(position, value)
print("After Insert :", numbers)

# // Remove
value = int(input("\nEnter Element to Remove : "))

if value in numbers:
    numbers.remove(value)
    print("After Remove :", numbers)
else:
    print("Element Not Found")

# // Pop
numbers.pop()
print("\nAfter Pop :", numbers)

# // Sort
numbers.sort()
print("After Sort :", numbers)

# // Reverse
numbers.reverse()
print("After Reverse :", numbers)

# // Count
value = int(input("\nEnter Element to Count : "))
print("Count :", numbers.count(value))

# // Index
value = int(input("\nEnter Element to Find Index : "))

if value in numbers:
    print("Index :", numbers.index(value))
else:
    print("Element Not Found")

# // Copy
copyList = numbers.copy()
print("\nCopied List :", copyList)

# // Length
print("Length :", len(numbers))

# // Clear
choice = input("\nDo You Want to Clear List? (Y/N) : ")

if choice.upper() == "Y":
    numbers.clear()
    print("List After Clear :", numbers)
else:
    print("List Not Cleared :", numbers)
