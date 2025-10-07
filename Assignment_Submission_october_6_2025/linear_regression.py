import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

rng = np.random.default_rng(42)
X = rng.uniform(0, 100, size=(200, 1))  # feature
y = 3 * X.squeeze() + 7 + rng.normal(0, 10, size=200)  # target with noise

# Spliting into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

#Results
print("Coefficient (slope):", model.coef_[0])
print("Intercept:", model.intercept_)
print("R^2 Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
