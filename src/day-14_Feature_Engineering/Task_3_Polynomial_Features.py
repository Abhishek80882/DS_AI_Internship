import pandas as pd
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Dataset
data = {"Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Score": [50, 55, 65, 80, 100, 125, 155, 190, 230, 275]}
df = pd.DataFrame(data)

# Split features and target
X = df[["Hours_Studied"]]
y = df["Score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train_scaled, y_train)
linear_preds = linear_model.predict(X_test_scaled)
linear_score = r2_score(y_test, linear_preds)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
poly_preds = poly_model.predict(X_test_poly)
poly_score = r2_score(y_test, poly_preds)

print(f'Linear Model R2: {linear_score:.2f}')
print("Polynomial Model R2:", poly_score)
