"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""
from functions import file_analyze

fh = open('foods.txt', 'r', encoding='utf-8')

print(file_analyze(fh))

fh.close()
