# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

import csv

def analyze_financial_data():
    filename = input("File to analyze: ").strip()
    closing_prices = []

    with open(filename, mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_close = row["Close"].strip()
            cleaned_close = raw_close.replace("€", "").replace("$", "").replace(",", "")
            if cleaned_close:
                closing_prices.append(float(cleaned_close))

    most_recent_close = closing_prices[-1]
    average_close = sum(closing_prices) / len(closing_prices)

    print(f"The average closing price was {average_close:.2f}.")

    if most_recent_close > average_close:
        print(f"The most recent closing price ({most_recent_close}) was above the average.")
    elif most_recent_close < average_close:
        print(f"The most recent closing price ({most_recent_close}) was below the average.")
    else:
        print(f"The most recent closing price ({most_recent_close}) was equal to the average.")

if __name__ == "__main__":
    analyze_financial_data()
