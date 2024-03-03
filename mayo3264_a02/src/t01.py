"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
from Food_utilities import by_origin, read_foods

fh = open('foods.txt', 'r', encoding='utf-8')
food_list = by_origin(read_foods(fh), 3)

for i in range(len(food_list)):
    print(food_list[i])
    print()

fh.close()
