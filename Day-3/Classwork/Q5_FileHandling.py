"""
================================================================
                    Python Workshop - LJU
----------------------------------------------------------------
Program Name        : File Handling
Topic               : File Handling
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

File Handling is used to store and retrieve data permanently
from files.

Write a Python program to demonstrate various File Handling
operations and commonly used methods.

The program should perform the following operations:

1. Create File
2. Write Data
3. Read Complete File
4. Read One Line
5. Read All Lines
6. Append Data
7. Display File Pointer Position (tell())
8. Change File Pointer Position (seek())
9. Close File
10. Delete File (Optional)

================================================================
"""

import os

fileName = "Student.txt"

while True:

    print("\n========== FILE HANDLING ==========")
    print("1. Create File")
    print("2. Write Data")
    print("3. Read Complete File")
    print("4. Read One Line")
    print("5. Read All Lines")
    print("6. Append Data")
    print("7. tell() Method")
    print("8. seek() Method")
    print("9. Delete File")
    print("10. Exit")

    choice = int(input("\nEnter Choice : "))

    # // Create File
    if choice == 1:

        file = open(fileName, "w")
        file.close()

        print("File Created Successfully.")

    # // Write Data
    elif choice == 2:

        file = open(fileName, "w")

        data = input("Enter Data : ")

        file.write(data)

        file.close()

        print("Data Written Successfully.")

    # // Read Complete File
    elif choice == 3:

        try:

            file = open(fileName, "r")

            print("\nFile Content:\n")
            print(file.read())

            file.close()

        except FileNotFoundError:

            print("File Not Found.")

    # // Read One Line
    elif choice == 4:

        try:

            file = open(fileName, "r")

            print(file.readline())

            file.close()

        except FileNotFoundError:

            print("File Not Found.")

    # // Read All Lines
    elif choice == 5:

        try:

            file = open(fileName, "r")

            print(file.readlines())

            file.close()

        except FileNotFoundError:

            print("File Not Found.")

    # // Append Data
    elif choice == 6:

        file = open(fileName, "a")

        data = input("Enter Data : ")

        file.write("\n" + data)

        file.close()

        print("Data Appended Successfully.")

    # // tell() Method
    elif choice == 7:

        try:

            file = open(fileName, "r")

            print("Current Position :", file.tell())

            file.read()

            print("After Reading :", file.tell())

            file.close()

        except FileNotFoundError:

            print("File Not Found.")

    # // seek() Method
    elif choice == 8:

        try:

            file = open(fileName, "r")

            position = int(input("Enter Position : "))

            file.seek(position)

            print(file.read())

            file.close()

        except FileNotFoundError:

            print("File Not Found.")

    # // Delete File
    elif choice == 9:

        if os.path.exists(fileName):

            os.remove(fileName)

            print("File Deleted Successfully.")

        else:

            print("File Not Found.")

    # // Exit
    elif choice == 10:

        print("Thank You...")

        break

    else:

        print("Invalid Choice.")
