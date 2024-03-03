"""
-------------------------------------------------------
Lab 1, Task 6
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
from Food_utilities import write_foods, read_foods

fh = open('new_foods.txt', 'w', encoding='utf-8')
fh_old = open("foods.txt", 'r', encoding='utf-8')

write_foods(fh, read_foods(fh_old))

fh.close()
fh_old.close()
