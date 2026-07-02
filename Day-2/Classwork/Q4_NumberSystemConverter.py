"""
===============================================================
                    Python Workshop - LJU
---------------------------------------------------------------
Program Name        : Decimal Number System Converter
Topic               : While Loop Menu Driven
Language            : Python 3
Course              : MCA
University          : LJU
Author              : Mohmadhusen Khimani
===============================================================

Menu

1. Decimal to Binary
2. Decimal to Octal
3. Decimal to Hexadecimal
9. Exit

===============================================================
"""

while True:

    print("\n========== MENU ==========")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("9. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 9:
        print("Thank You...")
        break

    number = int(input("Enter Decimal Number : "))

    if choice == 1:
        print("Binary :",bin(number))

    elif choice == 2:
        print("Octal :",oct(number))

    elif choice == 3:
        print("Hexadecimal :",hex(number))

    else:
        print("Invalid Choice")