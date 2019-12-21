import numpy as np
from colorama import Fore, Style


def red_text(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"


class Ruler():
    """classe pour mesurer la distance entre deux chaines
    en utilisant l'algorithme de Needleman-Wunsch"""

    match_score = 1
    dismatch_score = -1
    gap_score = -1
    length = 0
    width = 0
    coef_mat = np.zeros([0, 0])
    distance = 0
    res_up = ""
    res_low = ""

    def __init__(self, upper: str, lower: str):
        self.upper = '-' + upper
        self.lower = '-' + lower
        self.length = len(upper) + 1
        self.width = len(lower) + 1
        self.coef_mat = np.zeros([self.length, self.width])

    def build_matrix(self):
        self.coef_mat[0] = np.arange(self.width)*self.gap_score
        for i in range(1, self.length):
            self.coef_mat[i][0] = self.gap_score*i
            for j in range(1, self.width):
                if self.upper[i] == self.lower[j]:
                    val = self.match_score
                else:
                    val = self.dismatch_score
                self.coef_mat[i][j] = max([
                    self.coef_mat[i-1][j] + self.gap_score,
                    self.coef_mat[i][j-1] + self.gap_score,
                    self.coef_mat[i-1][j-1] + val
                    ])

    def rebuild(self):
        res_upper = ""
        res_lower = ""
        i = self.length - 1
        j = self.width - 1
        while (i > 0 and j > 0):
            # print(i, j, res_upper, res_lower)
            if self.upper[i] == self.lower[j]:
                val = self.match_score
                self.distance -= 1
            else:
                val = self.dismatch_score
            if (self.coef_mat[i][j] ==
                    self.coef_mat[i-1][j-1] + val):
                res_upper = self.upper[i] + res_upper
                res_lower = self.lower[j] + res_lower
                i -= 1
                j -= 1
            elif (self.coef_mat[i][j] ==
                    self.coef_mat[i-1][j] + self.gap_score):
                res_upper = self.upper[i] + res_upper
                res_lower = "=" + res_lower
                i -= 1
            elif (self.coef_mat[i][j] ==
                    self.coef_mat[i][j-1] + self.gap_score):
                res_upper = "=" + res_upper
                res_lower = self.lower[j] + res_lower
                j -= 1
            else:
                raise ValueError
            self.distance += 1
        # print("Rebuild finished. ")
        # print(res_upper)
        # print(res_lower)
        self.res_up, self.res_low = res_upper, res_lower

    def compute(self):
        self.build_matrix()
        self.rebuild()

    def report(self):
        return self.res_up, self.res_low


str1 = "GGATCGA"
str2 = "GAATTCAGTTA"
str1 = "abcdefghi"
str2 = "abcdfghi"
ruler = Ruler(str1, str2)
ruler.compute()
# print(ruler.length, ruler.width)
# print(ruler.coef_mat)
print(ruler.distance)
top, bottom = ruler.report()
print(top)
print(bottom)

message = "def"
print(f"abc{red_text(message)}ghi")
