"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
from Queue_circular import Queue

queue1 = Queue()
queue2 = Queue()
print('Empty:', queue1.is_empty())
for i in range(10):
    queue1.insert(i)
    queue2.insert(i)
print("Length:", len(queue1))
queue2.remove()
queue2.insert(100)
print('Empty:', queue1.is_empty())
print('Equals:', queue1 == queue2)

for i in range(len(queue1)):
    print(queue1.remove())
print('Full:', queue1.is_full())
