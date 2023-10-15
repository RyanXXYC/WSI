import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


# Reading the CSV file directly
try :
    # Specify data types for multiple columns
    dtype_dict = {
        'Impedance Magnitude (Ohms)': float,
        'Impedance Phase Degrees (I)': float,
        'Admittance Magnitude (S)': float,
        'Capacitance Magnitude (F)' : float
    # Add more columns as needed
    }
    columns_to_read = ['Point Number', 'Admittance Magnitude (S)']
    df = pd.read_csv("C:\\test2.csv", skiprows=3, dtype=dtype_dict, encoding='utf-8', na_values=['NaN', 'N/A', 'NA', 'nan'], usecols=columns_to_read)

    print(df.head())
except Exception as e:
    print(f"Error: {e}")

# Extracting Time and Capacitance columns
time = df['Point Number']
capacitance = df['Admittance Magnitude (S)']
#TODO: need to adjust data layout in csv file


# Convert time to minutes for plotting
def time_to_minutes(t):
    parts = [int(part) for part in str(t).split(":")]
    if len(parts) == 3:
        return parts[0] * 60 + parts[1] + parts[2] / 60
    elif len(parts) == 2:
        return parts[0] + parts[1] / 60
    else:
        return parts[0] / 60

minutes = [time_to_minutes(t) for t in time] #TODO: need to update this

# Adjust time data to start from the first data point
first_time = minutes[0]
minutes = [m - first_time for m in minutes]

# Convert Capacitance from F to pF
capacitance_pf = [c * 1e12 for c in capacitance]  # 1 F = 1e12 pF

#Plotting the Data
plt.figure(figsize=(10, 6))
plt.plot(minutes, capacitance_pf, marker='o', linestyle='-')
plt.title("Capacitance Magnitude vs Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Capacitance Magnitude (pF)")
plt.xlim(0, 2)  # Set x-axis limits to 0-2 minutes
plt.ylim(0, 100)  # Set y-axis limits to 0-100 pF
plt.grid(True)
plt.tight_layout()  # Adjusts the plot layout
plt.show(block = True)
