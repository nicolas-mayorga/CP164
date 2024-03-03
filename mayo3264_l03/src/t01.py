"""
-------------------------------------------------------
Lab 3, Task 1
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
from utilities import array_to_queue
from Queue_array import Queue

source = [11, 22, 33, 44]
queue = Queue()

array_to_queue(queue, source)
print(source)

for item in queue:
    print(item)
