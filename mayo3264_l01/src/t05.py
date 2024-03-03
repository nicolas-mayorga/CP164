"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
from Food_utilities import read_foods

fh = open("foods.txt", "r", encoding="utf-8")

print(read_foods(fh))

fh.close()
