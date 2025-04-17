import pandas as pd

# Load the CSV file into a DataFrame
trips_data = pd.read_csv("Trips_by_Distance.csv")

# Filter rows with over 10M trips in the 10-25 range
many_trips_10_25 = trips_data[trips_data['Number of Trips 10-25'] > 10_000_000]
# Filter rows with over 10M trips in the 50-100 range
many_trips_50_100 = trips_data[trips_data['Number of Trips 50-100'] > 10_000_000]

# Get unique dates from each filtered DataFrame
dates_for_10_25 = set(many_trips_10_25['Date'])
dates_for_50_100 = set(many_trips_50_100['Date'])

# Identify dates common to both categories and dates unique to each
common_dates = dates_for_10_25 & dates_for_50_100
unique_10_25 = dates_for_10_25 - dates_for_50_100
unique_50_100 = dates_for_50_100 - dates_for_10_25

# Print the results
print("Dates with >10M trips in BOTH 10–25 and 50–100 categories:")
print(sorted(common_dates))

print("\nDates with >10M trips in 10–25 only:")
print(sorted(unique_10_25))

print("\nDates with >10M trips in 50–100 only:")
print(sorted(unique_50_100))
