"""
================================================================
                    Python Workshop - LJU
----------------------------------------------------------------
Program Name        : Exception Handling
Topic               : Exception Handling
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

Exception Handling is used to handle runtime errors so that
the program does not terminate unexpectedly.

Write a Python program to demonstrate:

1. try
2. except
3. Multiple except
4. else
5. finally
6. raise Exception
7. User Defined Exception

================================================================
"""


# // User Defined Exception
class InvalidAgeError(Exception):
    pass


print("==============================")
print(" Exception Handling in Python ")
print("==============================")

# // Example 1 : try-except
print("\nExample 1 : try-except")

try:
    number = int(input("Enter a Number : "))
    print("Result :", 100 / number)

except:
    print("Error Occurred!")

# // Example 2 : Multiple Except
print("\nExample 2 : Multiple Except")

try:
    number = int(input("Enter Another Number : "))
    print("Result :", 100 / number)

except ZeroDivisionError:
    print("Cannot Divide by Zero.")

except ValueError:
    print("Please Enter Valid Integer.")

# // Example 3 : else
print("\nExample 3 : else")

try:
    number = int(input("Enter Number : "))
    print("Square :", number * number)

except ValueError:
    print("Invalid Input")

else:
    print("Program Executed Successfully.")

# // Example 4 : finally
print("\nExample 4 : finally")

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File Not Found.")

finally:
    print("Finally Block Always Executes.")

# // Example 5 : raise Exception
print("\nExample 5 : raise")

try:

    marks = int(input("Enter Marks : "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks Must be Between 0 and 100.")

    print("Marks :", marks)

except ValueError as message:
    print(message)

# // Example 6 : User Defined Exception
print("\nExample 6 : User Defined Exception")

try:

    age = int(input("Enter Age : "))

    if age < 18:
        raise InvalidAgeError("Age Must be 18 or Above.")

    print("Eligible for Voting.")

except InvalidAgeError as message:
    print(message)

print("\nProgram Finished Successfully.")
