"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Simple Calculator
Topic               : Operators
Concept             : Arithmetic Operations
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

Write a menu-driven Python program to perform
basic arithmetic operations.

Operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division

===============================================================
"""

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("\nEnter Choice : "))

if choice == 1:
    print("Answer =", a + b)

elif choice == 2:
    print("Answer =", a - b)

elif choice == 3:
    print("Answer =", a * b)

elif choice == 4:
    if b != 0:
        print("Answer =", a / b)
    else:
        print("Division by Zero is Not Possible")

else:
    print("Invalid Choice")