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


# scaling and PCA
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale, StandardScaler
scaler = StandardScaler()

X = df.loc[:, df.columns != 'Class']
y = df.loc[:,['Class']].values

data = scale(X)
# data = scaler.fit(X)
pca = PCA(n_components=10)
principalComponents = pca.fit_transform(data)
principalDf = pd.DataFrame(data = principalComponents, columns = ['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10'])
finalDf = pd.concat([principalDf, df[['Class']]], axis = 1)



# write transformed data
export_csv = finalDf.to_csv (r'insuranceclaimfraud.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
