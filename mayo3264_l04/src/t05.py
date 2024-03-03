"""
-------------------------------------------------------
Lab 4, Task 5
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-02-01"
-------------------------------------------------------
"""
from List_array import List

source = List()

source.append(10)
source.append(20)
source.append(30)

source[1] = 5

for item in source:
    print(item)

print(source[0])
