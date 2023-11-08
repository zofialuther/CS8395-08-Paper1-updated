import pandas as pd

# load data from csv files
df_patients = pd.read_csv ('patients.csv', sep = ",", decimal=".")
df_visits = pd.read_csv ('visits.csv', sep = ",", decimal=".")

# typecast from string to datetime so .agg can 'max' it
df_visits['VISIT_DATE'] = pd.to_datetime(df_visits['VISIT_DATE'])

# merge on PATIENT_ID
df_merge = df_patients.merge(df_visits, on='PATIENT_ID', how='left')

# groupby is an intermediate object
df_group = df_merge.groupby(['PATIENT_ID','LASTNAME'], as_index=False)

# note: you can use 'sum' instead of the lambda function but that returns NaN as 0 (zero)
df_result = df_group.agg({'VISIT_DATE': 'max', 'SCORE': [lambda x: x.sum(min_count=1),'mean']})

print(df_result)