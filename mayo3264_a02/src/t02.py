"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
from Food_utilities import average_calories, read_foods

fh = open('foods.txt', 'r', encoding='utf-8')

avg_cals = average_calories(read_foods(fh))
print(avg_cals)

fh.close()
