"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
from Queue_array import Queue

queue1 = Queue()
queue2 = Queue()

for i in range(10):
    queue1.insert(i)
    queue2.insert(i)


print('Equals:', queue1 == queue2)
