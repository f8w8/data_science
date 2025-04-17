
import pandas as pd


# Load the CSV data containing trip distances into a DataFrame
df_dist = pd.read_csv("Trips_by_Distance.csv")

print (df_dist.head())
print (df_dist.info())

# Compute the rounded average of the 'Population Staying at Home' column 
# for records where the 'Level' is "National", then print it.
national_avg = df_dist[df_dist["Level"] == "National"]["Population Staying at Home"].mean().round()
print(national_avg)

# Calculate the total distance for each record by assigning an average distance 
# value to each trip range and summing them up.
df_dist['Total Distance'] = (
    df_dist['Number of Trips <1'] * 0.5 +
    df_dist['Number of Trips 1-3'] * 2 +
    df_dist['Number of Trips 3-5'] * 4 +
    df_dist['Number of Trips 5-10'] * 7.5 +
    df_dist['Number of Trips 10-25'] * 17.5 +
    df_dist['Number of Trips 25-50'] * 37.5 +
    df_dist['Number of Trips 50-100'] * 75 +
    df_dist['Number of Trips 100-250'] * 175 +
    df_dist['Number of Trips 250-500'] * 375 +
    df_dist['Number of Trips >=500'] * 600
)

# Determine the average distance traveled per person who left home 
# by dividing the total distance sum by the total number of people not staying at home.
df_dist['Avg Distance Per Person'] = df_dist['Total Distance'].sum() / df_dist['Population Not Staying at Home'].sum()

# Print the rounded average distance per person.
print(df_dist["Avg Distance Per Person"].mean().round())
