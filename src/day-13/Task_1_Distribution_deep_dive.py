import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('housing.csv')
sns.set(style='whitegrid')

# Numerical Data
sns.histplot(df['Price'], kde = True)
plt.show()

# Skewness And Kurtosis
print(f'Skewness : {df['Price'].skew():.2f}')
print(f'Kurtosis : {df['Price'].kurt():.2f}')

# Categorical Column
sns.countplot(x='City',data=df)
plt.show()