"""
-------------------------------------------------------
Lab 7, Task 1 
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-03-02"
-------------------------------------------------------
"""
from List_linked import List

source = List()
source2 = List()
target = List()

source.append(1)
source.append(2)
source.append(3)
source.append(4)

source2.append(5)
source2.append(6)
source2.append(7)
source2.append(8)

source.reverse_r()

for item in source:
    print(item)

target1, target2 = source.split_alt_r()

print(source._rear)

print()

for item in target1:
    print(item)
print('-----------')
for item in target2:
    print(item)
