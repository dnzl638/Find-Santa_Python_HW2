# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

import urllib.request

url = "https://study.find-santa.eu/data/py/fc.txt"

response = urllib.request.urlopen(url)
lines = response.read().decode("utf-8").splitlines()

weekend_temps = []

for line in lines:
  if "Saturday" in line or "Sunday" in line:
    parts = line.split()
    for part in parts:
      try:
        temp = float(part.replace("C", "").replace("°", ""))
        weekend_temps.append(temp)
      except ValueError:
        continue

avg_temp = sum(weekend_temps) / len(weekend_temps)

if avg_temp > 25:
  activity = "swimming"
elif avg_temp > 12:
  activity = "hiking"
elif avg_temp > 5:
  activity = "watching movies"
elif avg_temp > -5:
  activity = "relaxing in the local hot springs"
else:
  activity = "skiing"

print(f"Next weekend, {activity} would be a good activity.")
