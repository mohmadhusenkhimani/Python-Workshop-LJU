"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Fibonacci Series
Topic               : Function
Language            : Python 3
Course              : MCA
University          : LJU
Author              : Mohmadhusen Khimani
===============================================================
"""

def fibonacci(n):

    first = 0
    second = 1

    print(first,end=" ")
    print(second,end=" ")

    for i in range(n-2):

        third = first + second

        print(third,end=" ")

        first = second
        second = third

number = int(input("How Many Numbers : "))

fibonacci(number)