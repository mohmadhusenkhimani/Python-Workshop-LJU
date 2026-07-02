"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Museum Ticket Price
Topic               : Decision Making (Ladder If)
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
===============================================================

Question

A museum charges different ticket prices:

Age 5 to 18      -> ₹10
Age 19 to 64     -> ₹20
Age 65 and above -> ₹12

Use Ladder If to calculate the ticket price.

===============================================================
"""

age = int(input("Enter Age : "))

if age < 5:
    print("Entry is Free.")

elif age <= 18:
    print("Ticket Price : ₹10")

elif age <= 64:
    print("Ticket Price : ₹20")

else:
    print("Ticket Price : ₹12")