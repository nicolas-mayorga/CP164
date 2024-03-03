"""
-------------------------------------------------------
Assignment 1, Task 1 
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-02-13"
-------------------------------------------------------
"""
from List_array import List
from Food import Food

food1 = Food('Spaghetti', 7, True, 200)
food2 = Food('Ravioli', 7, True, 140)
food3 = Food('Hot Dog', 8, False, 500)
food4 = Food('Bacon Poutine', 0, False, 750)
food5 = Food('Banana milkshake', 3, True, 340)
food6 = Food('Jollof Rice', 9, True, 290)
food7 = Food('Country Style', 1, True, 400)
food8 = Food('Perogies', 10, True, 380)
food9 = Food('The Bev', 3, False, 1000)

lst1 = List()
lst2 = List()
lst3 = List()
lst4 = List()

target1 = List()
target2 = List()

target1.append(1)
target1.append(1)
target1.append(1)
target1.append(1)

lst1.append(food1)

lst2.append(food1)


for item in lst1:
    print(item)
    print()
print('_____________')
for item in lst2:
    print(item)
    print()
print('--------------------')

print(lst1 == lst2)
