"""
-------------------------------------------------------
Lab 6, Task 1
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-02-16"
-------------------------------------------------------
"""
from List_linked import List

source = List()


source.append(22)
source.append(33)
source.append(44)
source.append(55)

source.insert(2, 44)
print()
for item in source:
    print(item)
