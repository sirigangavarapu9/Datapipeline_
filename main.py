import pandas as pd

# Step 1: Extract data from the source CSV file
data = pd.read_csv('dummy_data.csv')

# Step 2: Perform any necessary data transformations
# Example: Sorting the data by age in descending order
transformed_data = data.sort_values(by='Age', ascending=False)

# Step 3: Load the transformed data into a target destination
# Example: Saving the transformed data as a new CSV file
transformed_data.to_csv('transformed_data.csv', index=False)

print("Data pipeline execution completed.")
