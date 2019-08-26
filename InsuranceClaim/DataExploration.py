import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# read insurance raw data
df = pd.read_csv("insuranceclaim.csv", sep=",")
df.head(10)

df['police_report_available'] = df['police_report_available'].replace("?", 'NO')
df['collision_type'] = df['collision_type'].replace("?", 'Rear Collision')
df['property_damage'] = df['property_damage'].replace("?", 'NO')

# df.columns = [col.replace('?', 'NO') for col in df.columns]
# df.columns = [col.replace('?', 'NO') for col in df.columns]
# collision_type
df.head(10)


# find out unique distinct values of each column
df.nunique()

# drop column having more distinct values
df = df.drop(["_c39","fraud_reported","policy_number", "policy_bind_date", "insured_zip", "incident_location", "incident_date"], axis=1)

# factorize the string columns and convert it into integer
for col in df.columns[df.dtypes == object]:
    df[col] = pd.factorize(df[col])[0]
