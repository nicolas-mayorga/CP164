"""
-------------------------------------------------------
Assignment 7, Task 1
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-03-10"
-------------------------------------------------------
"""
from List_linked import List

source1 = List()
source2 = List()
target = List()

source1.append(1)


source1.remove_many(10)

for item in source1:
    print(item)
