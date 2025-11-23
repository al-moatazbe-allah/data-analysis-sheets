import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Factory_data.csv")

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Summary stats
print(df.describe())

# Group by machine
machine_power = df.groupby("machine_id")['power_kw'].sum()
machine_power.plot(kind="bar", title="Total Power Consumption per Machine")
plt.xlabel("Machine ID")
plt.ylabel("Power (kW)")
plt.show()

# Power over time
plt.plot(df['timestamp'], df['power_kw'])
plt.title("Power Consumption Over Time")
plt.xlabel("Time")
plt.ylabel("Power (kW)")
plt.xticks(rotation=45)
plt.show()

# Group by shift
shift_power = df.groupby("shift")['power_kw'].mean()
shift_power.plot(kind="bar", color='orange', title="Average Power per Shift")
plt.ylabel("Power (kW)")
plt.show()

# Relationship between production and power
plt.scatter(df["production_units"], df["power_kw"])
plt.title("Production vs Power Consumption")
plt.xlabel("Production Units")
plt.ylabel("Power (kW)")
plt.show()
