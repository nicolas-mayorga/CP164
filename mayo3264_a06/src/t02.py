"""
-------------------------------------------------------
Assignment 6, Task 2
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
from Priority_Queue_linked import Priority_Queue

source1 = Priority_Queue()
target1 = Priority_Queue()

target2 = Priority_Queue()

source1.insert(99)


target1, target2 = source1.split_key(98)

for item in target1:
    print('target1')
    print(item)
print()
for item in target2:
    print('target2')
    print(item)
