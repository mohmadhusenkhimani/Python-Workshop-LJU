"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Lambda Functions
Topic               : Lambda Expression
Language            : Python 3
Course              : MCA
University          : LJU
Author              : Mohmadhusen Khimani
===============================================================

Operations

1. Square Number
2. Even or Odd
3. Celsius to Fahrenheit
4. Largest of Two Numbers

===============================================================
"""

# Square

square = lambda x : x*x

num = int(input("Enter Number : "))

print("Square :",square(num))

print()

# Even Odd

evenodd = lambda x : "Even" if x%2==0 else "Odd"

num = int(input("Enter Number : "))

print(evenodd(num))

print()

# Celsius to Fahrenheit

convert = lambda c : (c*9/5)+32

temp = float(input("Enter Celsius : "))

print("Fahrenheit :",convert(temp))

print()

# Largest Number

largest = lambda a,b : a if a>b else b

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

print("Largest Number :",largest(num1,num2))