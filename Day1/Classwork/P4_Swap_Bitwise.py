"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Swap without Third Variable
Topic               : Bitwise Operators
Concept             : XOR Operator
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

Write a Python program to swap two numbers without using
a third variable using the Bitwise XOR (^) operator.

===============================================================
"""

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

print("\nBefore Swapping")
print("A =", a)
print("B =", b)

a = a ^ b
b = a ^ b
a = a ^ b

print("\nAfter Swapping")
print("A =", a)
print("B =", b)