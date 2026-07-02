"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Write a Function
Topic               : HackerRank - Introduction
Concept             : Functions
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question:

Complete the function leap_year().

Return True if the given year is a leap year;
otherwise return False.

Rules:

• Divisible by 400 → Leap Year
• Divisible by 100 → Not Leap Year
• Divisible by 4 → Leap Year
• Otherwise → Not Leap Year

===============================================================
"""

def is_leap(year):

    leap = False

    if year % 400 == 0:
        leap = True

    elif year % 100 == 0:
        leap = False

    elif year % 4 == 0:
        leap = True

    return leap


year = int(input())
print(is_leap(year))