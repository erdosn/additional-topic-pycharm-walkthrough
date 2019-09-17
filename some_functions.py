import numpy as np


def pythagorean_theorem(a, b):
    return np.sqrt(a**2 + b**2)


if __name__=="__main__":
    a = 4
    b = 10
    c = pythagorean_theorem(a, b)
    print(c)