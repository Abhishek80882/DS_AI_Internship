import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('housing.csv')
sns.set(style='whitegrid')

#Correlation
correlation = df.corr(numeric_only=True)
print(correlation)

sns.heatmap(correlation, annot =True, cmap='coolwarm')
plt.show()

# Box-Plot 
sns.boxplot(df['Price'])
plt.show()

print(f"\nStatistical Summary : \n{df.describe()}")

