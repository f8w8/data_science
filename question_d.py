from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Select trip features from different distance bands
trip_features = df_dist[[
    'Number of Trips <1',
    'Number of Trips 1-3',
    'Number of Trips 3-5',
    'Number of Trips 5-10',
    'Number of Trips 10-25',
    'Number of Trips 25-50',
    'Number of Trips 50-100',
    'Number of Trips 100-250',
    'Number of Trips 250-500',
    'Number of Trips >=500'
]]
trip_features = trip_features.fillna(trip_features.mean())

# Set target variable as the population not staying at home
stay_out_population = df_dist['Population Not Staying at Home']
stay_out_population = stay_out_population.fillna(stay_out_population.mean())

# Split data into training and testing sets
features_train, features_test, target_train, target_test = train_test_split(
    trip_features, stay_out_population, test_size=0.2, random_state=42
)

# Create and train the linear regression model
regression_model = LinearRegression()
regression_model.fit(features_train, target_train)

# Make predictions on the test data
predictions = regression_model.predict(features_test)

# Compute evaluation metrics
mse_error = mean_squared_error(target_test, predictions)
print("Mean Squared Error:", round(mse_error))

r2_value = r2_score(target_test, predictions)
print("R-squared:", round(r2_value, 4))

# Print the sorted coefficients to show feature importance
coefficients = pd.Series(regression_model.coef_, index=trip_features.columns)
print("\nModel coefficients (importance of each trip type):")
print(coefficients.sort_values(ascending=False))
