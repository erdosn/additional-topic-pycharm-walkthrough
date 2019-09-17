import numpy as np

import some_functions as sf


def test_pythagorean_function_0():
    a = 0
    b = 00
    actual = sf.pythagorean_theorem(a, b)
    assert expected==actual, "failed first test"