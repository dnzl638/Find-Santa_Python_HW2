# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

denom = int(input('Denominator: '))
upp_lim = int(input('Upper limit: '))

total_sum = sum(range(denom, upp_lim + 1, denom))

print(f"Sum: {total_sum}")
