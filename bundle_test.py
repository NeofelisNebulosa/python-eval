import numpy as np
from needleman_wunsch import Ruler
import sys
import time

print(sys.argv)

with open(f"{sys.argv[1]}" + ".txt", "r") as f:
    data = f.read().splitlines()
    print(data)
    i = 0
    j = 1
    while i < len(data):
        while len(data[i]) == 0:
            i += 1
        str1 = data[i]
        if i == len(data)-1:
            break
        str2 = data[i+1]
        time_start = time.time()
        ruler = Ruler(str1, str2)
        ruler.compute()
        top, bottom = ruler.report()
        print(f"====== example # {j} - distance = {ruler.distance}")
        print(top)
        print(bottom)
        i += 2
        j += 1
        time_end = time.time()
        print('time cost', time_end - time_start, 's')
