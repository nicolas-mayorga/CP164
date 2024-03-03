"""
-------------------------------------------------------
Assignment 6, Task 1
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
from Queue_linked import Queue

source1 = Queue()
source2 = Queue()
target = Queue()


target.insert(11)
target.insert(22)
target.insert(33)
target.insert(44)

source1, source2 = target.split_alt()


source1.print()
source2.print()
