import numpy as np
from colorama import Fore, Style, init


def red_text(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"


class Ruler():
    """classe pour mesurer la distance entre deux chaines
    en utilisant l'algorithme de Needleman-Wunsch"""

    # These 5 parameters set the coefficients of the algorithme
    match_score = 1
    dismatch_score = -1
    gap_score = -1
    insert_cost = 1
    substitute_cost = 1

    # Default values of the class
    distance = "Available only after the compute operation. "
    __res_up = "Available only after the compute operation. "
    __res_low = "Available only after the compute operation. "

    # Initialization
    def __init__(self, upper: str, lower: str):
        self.upper = '-' + upper
        self.lower = '-' + lower
        self.length = len(upper) + 1
        self.width = len(lower) + 1
        self.coef_mat = np.zeros([self.length, self.width])

    # Construction of the weight matrix
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

    # Reconstruction of the 2 strings
    def rebuild(self):
        init()  # initialize colorama package
        res_upper = ""
        res_lower = ""
        i = self.length - 1
        j = self.width - 1

        # Reconstruction loop
        while (i > 0 and j > 0):
            # Check if matched
            if self.upper[i] == self.lower[j]:
                val = self.match_score
            else:
                val = self.dismatch_score

            # Ascending to the upleft matrix element
            if (self.coef_mat[i][j] ==
                    self.coef_mat[i-1][j-1] + val):
                if self.upper[i] == self.lower[j]:
                    res_upper = self.upper[i] + res_upper
                    res_lower = self.lower[j] + res_lower
                else:
                    res_upper = red_text(self.upper[i]) + res_upper
                    res_lower = red_text(self.lower[j]) + res_lower
                    self.distance += self.substitute_cost
                i -= 1
                j -= 1

            # Ascending to the left matrix element
            elif (self.coef_mat[i][j] ==
                    self.coef_mat[i-1][j] + self.gap_score):
                res_upper = self.upper[i] + res_upper
                res_lower = red_text("=") + res_lower
                i -= 1
                self.distance += self.insert_cost

            # Ascending to the matrix element above
            elif (self.coef_mat[i][j] ==
                    self.coef_mat[i][j-1] + self.gap_score):
                res_upper = red_text("=") + res_upper
                res_lower = self.lower[j] + res_lower
                j -= 1
                self.distance += self.insert_cost
            else:
                raise ValueError("No matched element in the matrix. ")

        self.__res_up, self.__res_low = res_upper, res_lower

    # Compute the distance between 2 strings
    def compute(self):
        self.distance = 0
        self.build_matrix()
        self.rebuild()

    # Results feedback
    def report(self):
        return self.__res_up, self.__res_low
