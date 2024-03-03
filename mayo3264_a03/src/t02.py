"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
from Stack_array import Stack


source1 = Stack()
source2 = Stack()
target = Stack()

list1 = [1, 2, 3, 4]
list2 = [8, 7, 6, 5]

for item in list1:
    source1.push(item)

for item in list2:
    source2.push(item)

target.combine(source1, source2)

for item in target:
    print(item)
