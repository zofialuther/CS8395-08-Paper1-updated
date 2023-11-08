import pandas as pd

df_patients = pd.read_csv('patients.csv', sep=",", decimal=".")
df_visits = pd.read_csv('visits.csv', sep=",", decimal=".")

df_visits['VISIT_DATE'] = pd.to_datetime(df_visits['VISIT_DATE'])

df_merge = df_patients.merge(df_visits, on='PATIENT_ID', how='left')

df_group = df_merge.groupby(['PATIENT_ID','LASTNAME'], as_index=False)

df_result = df_group.agg({'VISIT_DATE': 'max', 'SCORE': [lambda x: x.sum(min_count=1),'mean']})

print(df_result)