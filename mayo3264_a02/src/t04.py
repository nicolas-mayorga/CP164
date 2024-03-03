"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
from Food_utilities import food_table, read_foods

fh = open('foods.txt', 'r', encoding='utf-8')

food_table(read_foods(fh))

fh.close()
