"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
from Stack_array import Stack

stack = Stack()

for i in range(1, 6):
    stack.push(i)


stack.reverse()

for item in stack:
    print(item)
