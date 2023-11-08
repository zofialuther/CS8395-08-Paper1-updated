import pandas as pd

# Read the csv file and create a dataframe
df = pd.read_csv('file.csv')

# Calculate the sum of each row
row_sums = df.sum(axis=1)

# Add a new column to the dataframe with the row sums
df['Row_Sums'] = row_sums

# Overwrite the original csv file with the updated dataframe
df.to_csv('file.csv', index=False)