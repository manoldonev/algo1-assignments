
""" Karatsuba Multiplication """

import math


def multiply(x, y):
    """
    x = 10^(n/2)*a + b, y = 10^(n/2)*c + d where a, b, c, d are n/2 digit numbers

    x*y = 10^(n)*a*c + 10^(n/2)*(a*d + b*c) + b*d
    1. Compute recursively a*c
    2. Compute recursively b*d
    3. Compute recursively (a + b)*(c + d) = a*c + b*c + a*d +b*d
    3) - 1) - 2) = a*d + b*c
    """
    if x < 0 or y < 0:
        raise ValueError("Negative integers not supported")

    if x < 10 or y < 10:
        return x * y

    n = max(int(math.log10(x)), int(math.log10(y))) + 1
    nby2 = n // 2

    a = x // 10**(nby2)
    b = x % 10**(nby2)
    c = y // 10**(nby2)
    d = y % 10**(nby2)

    a_c = multiply(a, c)
    b_d = multiply(b, d)
    a_d_plus_b_c = multiply(a + b, c + d) - a_c - b_d

    return 10**(2 * nby2) * a_c + 10**nby2 * a_d_plus_b_c + b_d
