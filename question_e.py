import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data
df_dist = pd.read_csv("Trips_by_Distance.csv")

# List of distance trip columns
trip_cols = [
    'Number of Trips <1',
    'Number of Trips 1-3',
    'Number of Trips 3-5',
    'Number of Trips 5-10',
    'Number of Trips 10-25',
    'Number of Trips 25-50',
    'Number of Trips 50-100',
    'Number of Trips 100-250',
    'Number of Trips 250-500',
    'Number of Trips >=500'  # Make sure this column name matches exactly in your CSV
]

# Sum total trips per distance category
total_trips_by_category = df_dist[trip_cols].sum()

# Create a histogram
fig, ax = plt.subplots(figsize=(8, 8))
# Create indices for each trip category
x = np.arange(len(trip_cols))
# Use np.arange with an offset to create bins so that each bin centers on the category index
ax.hist(x, bins=np.arange(-0.5, len(x) + 0.5, 1), weights=total_trips_by_category, edgecolor='black')

# Set x-ticks to display the distance categories
ax.set_xticks(x)
ax.set_xticklabels(trip_cols, rotation=45, ha='right')

ax.set_title("Trip Distribution by Distance")
ax.set_xlabel("Trip Distance Categories")
ax.set_ylabel("Number of Trips")

plt.tight_layout()
plt.show()
