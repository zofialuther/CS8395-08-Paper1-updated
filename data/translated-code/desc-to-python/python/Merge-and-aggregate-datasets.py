import pandas as pd

# Load patient and visit data from csv files
patient_data = pd.read_csv('patient_data.csv')
visit_data = pd.read_csv('visit_data.csv')

# Create data frames with hard-coded data
data = {'patient_id': [1, 2, 3], 'visit_date': ['2022-01-01', '2022-02-01', '2022-03-01'], 'visit_score': [8, 7, 9]}
df = pd.DataFrame(data)

# Typecast visit date from string to datetime
df['visit_date'] = pd.to_datetime(df['visit_date'])

# Merge patient and visit data on patient ID
merged_data = pd.merge(patient_data, visit_data, on='patient_id')

# Group the data and aggregate to find maximum visit date and calculate sum and mean of visit scores
grouped_data = merged_data.groupby('patient_id').agg({'visit_date': 'max', 'visit_score': ['sum', 'mean']})

# Print the resulting data frame
print(grouped_data)