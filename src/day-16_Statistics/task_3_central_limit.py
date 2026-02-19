import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')

skewed_data = np.random.exponential(scale=20 , size= 1000)
df = pd.DataFrame({
                    'skewed_data': skewed_data
                 })

mean = df['skewed_data'].mean()
print(f'Mean : {mean:.2f}')

sample_data = []
for i in range(1000):
    sample = np.random.choice(df['skewed_data'],size=30)
    sample_data.append(sample.mean())

plt.figure()
sns.histplot(sample_data,kde=True)
plt.xlabel('Skewed Data')
plt.ylabel('Frequency')
plt.show()
