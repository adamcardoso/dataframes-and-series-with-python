import pandas as pd

data = pd.read_csv('lsd_math_score_data.csv')  # Read the data
print(data)  # Print the whole data frame

print(data['Avg_Math_Test_Score'])  # Print a column
only_math_scores = data['Avg_Math_Test_Score']  # Get a column
print(only_math_scores)  # Print only the math scores

data['High_Score'] = 100  # Add a new column
print(data)  # Print the whole data frame

data['High_Score'] = data['High_Score'] + data['Avg_Math_Test_Score']
print(data)  # Print the whole data frame

data['High_Score'] = data['High_Score'] * data['High_Score']
print(data)  # Print the whole data frame

data['High_Score'] = data['High_Score'] ** 2
print(data)  # Print the whole data frame