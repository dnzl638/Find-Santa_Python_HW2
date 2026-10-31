# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

from math import sqrt

import cmath

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
q = cmath.sqrt(b ** 2 - 4 * a * c)
x1 = (-b + q) / (2 * a)
x2 = (-b - q) / (2 * a)
print(f'x1: {x1:.2f} x2: {x2:.2f}')
