"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
from functions import queue_split_alt
from Queue_array import Queue

queue = Queue()

for i in range(10):
    queue.insert(i)

target1, target2 = queue_split_alt(queue)

for i in range(len(target1)):
    print(target1.remove())
    print(target2.remove())
