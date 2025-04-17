import dask
dask.config.set({"dataframe.convert-string": False})

import time
import pandas as pd
import dask.dataframe as dd
import matplotlib.pyplot as plt

# Define simulated processor counts and a dict to store times
processors = [10, 20]
times_record = {}

# Load CSV file into a Pandas DataFrame
df = pd.read_csv("Trips_by_Distance.csv")

# Convert the trip columns to numeric values
df["Number of Trips 10-25"] = pd.to_numeric(df["Number of Trips 10-25"], errors="coerce")
df["Number of Trips 50-100"] = pd.to_numeric(df["Number of Trips 50-100"], errors="coerce")

# Create a Dask DataFrame 
ddf = dd.from_pandas(df, npartitions=4)

# Loop to simulate parallel processing and timing
for proc in processors:
    print(f"\n=== Simulating processing with {proc} logical cores ===")
    start = time.time()

    # Filter rows where the 10-25 trips exceed 10M and compute the result
    filtered_10_25 = ddf[ddf["Number of Trips 10-25"] > 1e7][["Date", "Number of Trips 10-25"]].compute()

    # Filter rows where the 50-100 trips exceed 10M and compute the result
    filtered_50_100 = ddf[ddf["Number of Trips 50-100"] > 1e7][["Date", "Number of Trips 50-100"]].compute()

    elapsed = time.time() - start
    times_record[proc] = elapsed

    print(f"10-25 Trips (>10M): {len(filtered_10_25)} rows")
    print(f"50-100 Trips (>10M): {len(filtered_50_100)} rows")
    print(f"Time: {elapsed:.2f} seconds")

# Print the summary of processing times
print("\n=== Timing Summary ===")
for core, t in times_record.items():
    print(f"{core} processors: {t:.2f} seconds")
