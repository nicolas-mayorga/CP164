"""
-------------------------------------------------------
Assignment 6, Task 3
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
from Deque_linked import Deque

source1 = Deque()
source2 = Deque()

source1.insert_front(2)
source1.insert_front(1)
source1.insert_rear(3)
source1.remove_front()
source1.remove_rear()

source2.insert_front(0)
source2.insert_front(1)
source2.insert_front(2)
source2.insert_front(3)

l = source2._rear
r = source2._front._next

for item in source2:
    print(item)

source2._swap(l, r)

print(source1 == source2)

for item in source2:
    print(item)

print()
print(source2._rear._value)
