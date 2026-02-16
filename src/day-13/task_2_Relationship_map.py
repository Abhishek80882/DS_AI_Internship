import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('housing.csv')
sns.set(style = 'whitegrid')

# Scatter Plot
plt.figure()
sns.scatterplot(x='SquareFootage',y='Price',data = df)
plt.show()

# Box Plot
plt.figure()
sns.boxplot(x = 'City', y = 'SquareFootage',data = df)
plt.show()

print("As X increases, Y seems to increases")
