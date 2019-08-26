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

# percentage of dataddistribution
print("No Fraud '0': {} % of the dataset".format(round(df['Class'].value_counts(1)[0] * 100,2)))
print("Fraud '1': {} '% of the dataset \n".format(round(df['Class'].value_counts(1)[1] * 100,2)))
# plot bar chart
colors = ["#0101DF", "#DF0101"]

sns.countplot('Class', data=df, palette=colors)
plt.title('Class Distributions \n (0: No Fraud || 1: Fraud)', fontsize=14)
