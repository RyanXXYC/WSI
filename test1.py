import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import csv

data_by_columns = {}
def read_data(file_path, targets):
    header = None
    line_number = 0
    df = {target_name: [] for target_name in targets}

    with open(file_path, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            line_number += 1

            if line_number <= 3:
                # Skip the first three lines
                continue
            elif line_number == 4:
                # Process the fourth line
                header = row  # Assuming it's the header row
                continue
            
            row_as_floats = [float(col) if 'E' in col else col for col in row] # Convert scientific notationt to float
            
            for target in targets:
                # Updating dict
                df[target].append(row_as_floats[header.index(target)])
    return df


file_path = "C:\\test2.csv" # File name here
targets = ['Time', 'Capacitance Magnitude (F)'] # Add headers of data column here to read more data
df = read_data(file_path, targets)

time = df['Time']
capacitance = df['Capacitance Magnitude (F)']


# Convert time to minutes for plotting
def time_to_minutes(t):
    parts = [int(part) for part in str(t).split(":")]
    return parts[0] * 60 + parts[1] + parts[2] / 60
    

minutes = [time_to_minutes(t) for t in time] 

# Adjust time data to start from the first data point
first_time = minutes[0]
minutes = [m - first_time for m in minutes] # Here the first starting time is treated as "0" minutes in the plot

# Convert Capacitance from F to pF
capacitance_pf = [c * 1e12 for c in capacitance]  # 1 F = 1e12 pF

#Plotting the Data
plt.figure(figsize=(10, 6))
plt.plot(minutes, capacitance_pf, marker='o', linestyle='-')
plt.title("Capacitance Magnitude vs Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Capacitance Magnitude (pF)")
plt.xlim(min(minutes), max(minutes)) # Set x-axis limits to min to max in minutes
plt.ylim(min(capacitance_pf), max(capacitance_pf)) # Set y-axis to min to max in capacitance_pf
plt.grid(True)
plt.tight_layout()  # Adjusts the plot layout
plt.show()