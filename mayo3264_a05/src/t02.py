"""
-------------------------------------------------------
Assignment 5, Task 2
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-02-10"
-------------------------------------------------------
"""
from Sorted_List_array import Sorted_List
from Food import Food

food1 = Food('Spaghetti', 7, True, 200)
food2 = Food('Ravioli', 7, True, 140)
food3 = Food('Hot Dog', 8, False, 500)
food4 = Food('Bacon Poutine', 0, False, 750)
food5 = Food('Banana milkshake', 3, True, 340)

source1 = Sorted_List()
source2 = Sorted_List()

target1 = Sorted_List()
target2 = Sorted_List()

source1.insert(1)
source1.insert(1)
source1.insert(3)
source1.insert(4)
source1.insert(5)

source2.insert(1)
source2.insert(5)
source2.insert(9)
source2.insert(10)
source2.insert(1)

target1.intersection(source1, source2)


for item in target1:
    print(item)
