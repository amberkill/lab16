#Amber Kill 11-25-24 
# data pulled from Ohios unemployed archives showing from 1975-2002
#This is lab 16

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

date = []
un_rate = []

with open("OHUR.csv") as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header row
    header_row = next(reader)
    
    # Read through the actual data rows
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            un_rates = float(row[1])
            date.append(current_date)
            un_rate.append(un_rates)
        except ValueError:
            print(f"Skipping invalid row: {row}")  # Optional error handling
            continue

plt.style.use('ggplot')
figure, graph = plt.subplots()
graph.plot(date, un_rate, color='red')
graph.set_title('Ohio Unemployment Rate (1976-2002)')
graph.set_ylabel('Unemployment Rate')
figure.autofmt_xdate()
plt.show()