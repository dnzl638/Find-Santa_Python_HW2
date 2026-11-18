# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

n = int(input("Integer: "))
original_n = n

factors = []
divisor = 2

while divisor ** 2 <= n:
	while n % divisor == 0:
		factors.append(str(divisor))
		n //= divisor
	divisor += 1

if n > 1:
	factors.append(str(n))

print(f"{original_n} = {' * '.join(factors)}")
