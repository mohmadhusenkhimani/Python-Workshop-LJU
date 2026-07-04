"""
================================================================
                    Python Workshop - LJU
----------------------------------------------------------------
Program Name        : Stack and Queue
Topic               : Stack & Queue
Language            : Python 3
Course              : Master of Computer Applications (MCA)
University          : Lok Jagruti University (LJU)
Author              : Mohmadhusen Khimani
================================================================

Question:

Stack and Queue are two important linear data structures.

A Stack follows the LIFO (Last In First Out) principle,
where the last inserted element is removed first.

A Queue follows the FIFO (First In First Out) principle,
where the first inserted element is removed first.

Write a Python menu-driven program to perform the following
operations:

Stack Operations

1. Push
2. Pop
3. Display Stack

Queue Operations

4. Enqueue
5. Dequeue
6. Display Queue

7. Exit

================================================================
"""

# // Create Empty Stack and Queue
stack = []
queue = []

while True:

    print("\n========== STACK & QUEUE ==========")
    print("1. Stack Push")
    print("2. Stack Pop")
    print("3. Display Stack")
    print("4. Queue Enqueue")
    print("5. Queue Dequeue")
    print("6. Display Queue")
    print("7. Exit")

    choice = int(input("\nEnter Choice : "))

    # // Stack Push
    if choice == 1:

        element = int(input("Enter Element : "))
        stack.append(element)

        print("Element Pushed Successfully.")

    # // Stack Pop
    elif choice == 2:

        if len(stack) > 0:

            print("Removed Element :", stack.pop())

        else:

            print("Stack is Empty.")

    # // Display Stack
    elif choice == 3:

        if len(stack) > 0:

            print("Stack :", stack)

        else:

            print("Stack is Empty.")

    # // Queue Enqueue
    elif choice == 4:

        element = int(input("Enter Element : "))
        queue.append(element)

        print("Element Enqueued Successfully.")

    # // Queue Dequeue
    elif choice == 5:

        if len(queue) > 0:

            print("Removed Element :", queue.pop(0))

        else:

            print("Queue is Empty.")

    # // Display Queue
    elif choice == 6:

        if len(queue) > 0:

            print("Queue :", queue)

        else:

            print("Queue is Empty.")

    # // Exit
    elif choice == 7:

        print("\nThank You...")
        break

    # // Invalid Choice
    else:

        print("Invalid Choice. Please Try Again.")
