"""
-------------------------------------------------------
Lab 2, Task 1
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
from utilities import array_to_stack
from Stack_array import Stack

source = [99]
stack = Stack()

array_to_stack(stack, source)

for item in stack:
    print(item)
print(source)
