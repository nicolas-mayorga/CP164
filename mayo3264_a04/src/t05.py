"""
-------------------------------------------------------
Assignment 4, Task 5
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

queue = Priority_Queue()
key = 8

for i in range(10):
    queue.insert(i)

target1, target2 = pq_split_key(queue, key)

for item in target1:
    print(item)
print('––')
for item in target2:
    print(item)
