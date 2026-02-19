import numpy as np
import pandas as pd
import seaborn as sns
sns.set(style="whitegrid")

df = pd.DataFrame({
    'scores' :[72, 75, 78, 70, 74,76, 73, 77, 
               79, 71,80, 82, 69, 68, 74,73, 75, 200, 30, 76]
})

mean = df["scores"].mean()
std = df["scores"].std()
print(f'Mean : {mean:2f}\nstandard deviation : {std:.2f}\n')

df['z_score'] = (df['scores'] - mean) / std
print(f'{df}')

outliers = df[np.abs(df['z_score'] > 3)]
print("\nNumber of Outliers Detected:", len(outliers))
print(outliers)
