# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

x = 0

upper_limit = int(input(f'Upper limit: '))

while x <= upper_limit:
	sq = x ** 2

	if sq > upper_limit:
		break

	print(sq)

	x += 2
