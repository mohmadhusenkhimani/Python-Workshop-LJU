"""
================================================================
                    Python Workshop - LJU
----------------------------------------------------------------
Program Name        : String Methods
Topic               : String
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

Strings are one of the most commonly used data types in Python.

Write a Python program that demonstrates the commonly used
String methods.

The program should perform the following operations:

1. Convert to Uppercase
2. Convert to Lowercase
3. Capitalize String
4. Title Case
5. Swap Case
6. Remove Extra Spaces
7. Replace Word
8. Find a Word
9. Count Occurrences
10. Check Starts With
11. Check Ends With
12. Split String
13. Join String
14. Check Alphabet
15. Check Digits
16. Check Alphanumeric
17. Display String Length

================================================================
"""

# // Input String
text = input("Enter a String : ")

print("\n========== STRING METHODS ==========")

# // Convert to Uppercase
print("Upper Case          :", text.upper())

# // Convert to Lowercase
print("Lower Case          :", text.lower())

# // Capitalize First Letter
print("Capitalize          :", text.capitalize())

# // Title Case
print("Title Case          :", text.title())

# // Swap Uppercase and Lowercase
print("Swap Case           :", text.swapcase())

# // Remove Spaces
print("Strip               :", text.strip())

# // Replace Word
oldWord = input("\nEnter Word to Replace : ")
newWord = input("Enter New Word        : ")
print("Replace              :", text.replace(oldWord, newWord))

# // Find Word
findWord = input("\nEnter Word to Find : ")

if findWord in text:
    print("Found at Index      :", text.find(findWord))
else:
    print("Word Not Found")

# // Count Word
countWord = input("\nEnter Word to Count : ")
print("Count               :", text.count(countWord))

# // Starts With
startWord = input("\nStarts With : ")
print(text.startswith(startWord))

# // Ends With
endWord = input("Ends With   : ")
print(text.endswith(endWord))

# // Split String
print("\nSplit               :", text.split())

# // Join String
words = text.split()
print("Join                :", "-".join(words))

# // Check Alphabet
print("\nIs Alphabet         :", text.isalpha())

# // Check Digits
print("Is Digit            :", text.isdigit())

# // Check AlphaNumeric
print("Is AlphaNumeric     :", text.isalnum())

# // Display Length
print("Length              :", len(text))
