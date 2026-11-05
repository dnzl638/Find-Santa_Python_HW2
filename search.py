# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

files_input = input("Files: ")
needle = input("Needle: ")

filesnames = [name.strip() for name in files_input.split(',')]

total_occurences = 0

for filename in filesnames:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().lower()

            total_occurences += content.count(needle)

    except FileNotFoundError:
        print(f"Warning: File '{filename}' not found.")

print(f"Occurrences: {total_occurences}")
