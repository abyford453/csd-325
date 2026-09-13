"""
Title: sitka_high_low_db.py
Author: Armond Drew Byford
Course: CSD-325
Assignment: Module 4.2 - High/Low Temperatures

Purpose:
This program reads weather data from Sitka, Alaska.
The user can choose to view daily high temperatures,
daily low temperatures, or exit the program.
"""

import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt


# Open the weather data file and read the dates,
# high temperatures, and low temperatures.
filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)


# Display the program menu until the user chooses to exit.
while True:
    print("\nSitka Weather Program")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")

    choice = input("Please select Highs, Lows, or Exit: ")

    # Display the high temperature graph.
    if choice == '1':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    # Display the low temperature graph.
    elif choice == '2':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    # Exit the program.
    elif choice == '3':
        print("Thank you for using the Sitka Weather Program. Goodbye!")
        sys.exit()

    # Handle invalid menu selections.
    else:
        print("Invalid selection. Please choose 1, 2, or 3.")