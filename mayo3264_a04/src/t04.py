"""
-------------------------------------------------------
Assignment 4, Task 4
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
from Queue_array import Queue

queue = Queue()

target1 = Queue()
target2 = Queue()

for i in range(10):
    queue.insert(i)

target1, target2 = queue.split_alt()

for item in target1:
    print(item)

for item in target2:
    print(item)
