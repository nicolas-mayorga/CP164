"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
from Food_utilities import calories_by_origin, read_foods

fh = open('foods.txt', 'r', encoding='utf-8')

avg_cals = calories_by_origin(read_foods(fh), 4)
print(avg_cals)

fh.close()
