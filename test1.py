import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading the CSV file directly
df = pd.read_csv("c:\\Users\\20879\\Desktop\\garbage2\\test\\test.csv", skiprows=3)



# Extracting Time and Capacitance columns
time = df['Time']
capacitance = df['Capacitance Magnitude (F)']


# Convert time to minutes for plotting
def time_to_minutes(t):
    parts = [int(part) for part in str(t).split(":")]
    if len(parts) == 3:
        return parts[0] * 60 + parts[1] + parts[2] / 60
    elif len(parts) == 2:
        return parts[0] + parts[1] / 60
    else:
        return parts[0] / 60

minutes = [time_to_minutes(t) for t in time]

# Adjust time data to start from the first data point
first_time = minutes[0]
minutes = [m - first_time for m in minutes]

# Convert Capacitance from F to pF
capacitance_pf = [c * 1e12 for c in capacitance]  # 1 F = 1e12 pF

# Plotting the Data
plt.figure(figsize=(10, 6))
plt.plot(minutes, capacitance_pf, marker='o', linestyle='-')
plt.title("Capacitance Magnitude vs Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Capacitance Magnitude (pF)")
plt.xlim(0, 2)  # Set x-axis limits to 0-2 minutes
plt.ylim(0, 100)  # Set y-axis limits to 0-100 pF
plt.grid(True)
plt.tight_layout()  # Adjusts the plot layout
plt.show()