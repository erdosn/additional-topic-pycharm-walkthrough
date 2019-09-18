import numpy as np


def create_dictionary():
    d = {"a": 1, "b": "this is another value", "c": "here's another value"}

    d["d"] = "and the last value"

    return d


def pythagorean_theorem(a, b):
    return np.sqrt(a ** 2 + b ** 2)


def is_prime(n):
    if n == 2:
        return True
    top = int(n ** 0.5) + 1
    for i in range(2, top):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    a = 4
    b = 10
    c = pythagorean_theorem(a, b)
    print(c)
    print(create_dictionary())

    prime_number = 11
    print(is_prime(11))
