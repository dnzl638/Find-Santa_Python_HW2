# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

import math

radius = float(input('Enter the radius: '))
height = float(input('Enter the height: '))


surface = 2 * math.pi * radius * height
volume = ((math.pi * (height ** 2)) / 3) * (3 * radius - height)

print(f'The spherical cap has a surface of {surface:.3f}')
print(f'The volume of the spherical cap is {volume:.3f}')
