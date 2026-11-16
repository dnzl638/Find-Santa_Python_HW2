# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

import urllib.request

url = "https://study.find-santa.eu/data/py/r101.txt"
filename = "r101.txt"

urllib.request.urlretrieve(url, filename)

total_demand = 0.0

with open(filename, "r") as file:
    for line in file:
        parts = line.split()

        if len(parts) == 7 and parts[0].isdigit():
            demand = float(parts[3])
            total_demand += demand

print(f"Total demand: {total_demand}")
