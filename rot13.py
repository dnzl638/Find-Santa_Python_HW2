# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

filename = input("File to decode: ")

with open(filename, "r", encoding="utf-8") as file:
	content = file.read().upper()

decoded_chars = []

for char in content:
	code = ord(char)
	if 65 <= code <= 90:
		shifted = (code - 65 + 13) % 26 + 65
		decoded_chars.append(chr(shifted))
	else:
		decoded_chars.append(char)

print("".join(decoded_chars),end="")
