"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
from functions import stack_reverse
from Stack_array import Stack

stack = Stack()

for i in range(1, 3):
    stack.push(i)

stack_reverse(stack)

for item in stack:
    print(item)
