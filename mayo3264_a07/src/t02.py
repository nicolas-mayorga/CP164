"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-03-10"
-------------------------------------------------------
"""
from Sorted_List_linked import Sorted_List

source1 = Sorted_List()
source2 = Sorted_List()
target = Sorted_List()

source1.insert(11)
source1.insert(33)
source1.insert(55)

source2.insert(10)
source2.insert(44)
source2.insert(66)

target.combine(source1, source2)
for item in target:
    print(item)
