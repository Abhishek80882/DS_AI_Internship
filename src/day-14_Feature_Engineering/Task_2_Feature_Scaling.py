import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split

data = {
    "Age": [22, 25, 30, 35, 40, 45, 50, 28, 33, 38],
    "Salary": [20000, 25000, 30000, 50000, 60000, 80000, 100000, 28000, 45000, 70000]
}

df = pd.DataFrame(data)

X = df.drop('Salary', axis=1)
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardized
scaler = StandardScaler()
X_train_scaler = scaler.fit_transform(X_train)
X_test_scaler = scaler.transform(X_test)

#Min Max Scaling
minmax = MinMaxScaler()
X_train_minmax = minmax.fit_transform(X_train)
X_test_minmax = minmax.transform(X_test)


plt.figure()
plt.hist(df['Age'], bins=5)
plt.show()

plt.figure()
plt.hist(X_train_scaler)
plt.show()

plt.figure()
plt.hist(X_train_minmax[:, 0])
plt.show()
