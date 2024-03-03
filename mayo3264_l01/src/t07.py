"""
-------------------------------------------------------
Lab 1, Task 7
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
from Food_utilities import get_vegetarian, read_foods

fh = open('new_foods.txt', 'r', encoding='utf-8')

print(get_vegetarian(read_foods(fh)))

fh.close()
