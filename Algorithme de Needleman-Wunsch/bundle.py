import numpy as np
from needleman_wunsch import Ruler
import sys  # Package needed for data input


# Cet étape sert à ouvrir le ficher sous format TXT
try:
    filename = f"{sys.argv[1]}" + ".txt"
    f = open(filename, "r")  # Defaut file type is .txt

# En cas d'échec, on lance un demande de saisir
except FileNotFoundError:
    print("File not found or it is not a .txt file. ")
    new_filename = input("Please type in the complete filename: ")
    f = open(new_filename, "r")

finally:
    # Input data
    data = f.read().splitlines()
    data_length = len(data)

    # Content test
    if data_length < 1:
        raise Warning("Empty file. ")

    # Start of loop
    i = 0
    exp_count = 1
    while i < len(data):
        # Skip all empty lines
        while len(data[i]) == 0:
            i += 1

        # Ignore last single line
        if i == len(data)-1:
            break

        # Calculation
        str1 = data[i]
        str2 = data[i+1]
        ruler = Ruler(str1, str2)
        ruler.compute()
        top, bottom = ruler.report()
        print(f"====== example # {exp_count} - distance = {ruler.distance}")
        print(top)
        print(bottom)
        i += 2
        exp_count += 1

    f.close()
