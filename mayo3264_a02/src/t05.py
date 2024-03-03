"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
from Food_utilities import food_search, food_table, read_foods

fh = open('foods.txt', 'r', encoding='utf-8')

food_list = read_foods(fh)
food_table(food_search(food_list, 4, 150, True))

fh.close()
