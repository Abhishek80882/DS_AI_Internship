import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Age": [25,30,35,40,28,32,45,50,2,150,29,41],
    "Salary": [30000,40000,50000,65000,42000,48000,80000,90000,28000,52000,46000,70000],
    "Experience": [1,3,7,10,2,5,15,20,1,8,4,12],
    "Department": ["IT","HR","IT","Finance","HR","IT","Finance","Finance","HR","IT","HR","Finance"],
    "Gender": ["M","F","M","M","F","F","M","M","F","F","M","F"]
}
df = pd.DataFrame(data)

# print(df.shape)
# print(df.head())
# print(df.info())
# print(df.describe())

sns.boxplot(x="Age",data=df)
plt.show()

sns.histplot(df['Age'],kde=True)
plt.show()


sns.histplot(df['Salary'],kde=True)
plt.show()

sns.boxplot(x='Salary',data = df)
plt.show()


print(df['Age'].value_counts())
print(df['Department'].value_counts())

sns.countplot(x='Age',data = df)
plt.show()

plt.figure()
sns.scatterplot(x = 'Age',y='Salary', data=df)
plt.show()

correlation = df.corr(numeric_only = True)
print(correlation)

sns.heatmap(correlation,annot = True, cmap='coolwarm')
plt.show()