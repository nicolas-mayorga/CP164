"""
-------------------------------------------------------
Lab 2, Task 5
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-15"
-------------------------------------------------------
"""
from utilities import stack_test
from Food_utilities import read_foods
fh = open('foods.txt', 'r', encoding='utf-8')

source = read_foods(fh)

stack_test(source)
