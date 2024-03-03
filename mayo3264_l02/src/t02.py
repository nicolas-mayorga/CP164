"""
-------------------------------------------------------
Lab 2, Task 2
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
from utilities import stack_to_array
from Stack_array import Stack
list = []

stack = Stack()

for i in range(10):
    stack.push(i)
for item in stack:
    print(item)

stack_to_array(stack, list)

print(list)
