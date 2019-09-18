import numpy as np

import some_functions as sf


# def test_pythagorean_function_0():
#     a = 0
#     b = 00
#     actual = sf.pythagorean_theorem(a, b)
#     assert expected==actual, "failed first test"




def test_is_prime_for_prime():
    number = 11
    expected = True
    actual = sf.is_prime(number)
    assert actual==expected, f"you failed to identify {number} as prime"