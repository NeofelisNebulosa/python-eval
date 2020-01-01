import numpy as np
from needleman_wunsch import Ruler

str1 = "GGATCGA"
str2 = "GAATTCAGTTA"
# str1 = "abcdeddddfghi"
# str2 = "abcdfghi"
ruler = Ruler(str1, str2)
ruler.compute()
# print(ruler.length, ruler.width)
# print(ruler.coef_mat)
print(ruler.distance)
top, bottom = ruler.report()
print(top)
print(bottom)
