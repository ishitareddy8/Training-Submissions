import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# Load the cleaned dataset
path = "Assignment_Submission_october_6_2025/flowers_cleaned.csv"
df = pd.read_csv(path)

print("Available columns:", list(df.columns))

# Use height to predict longevity
X = df[["height (cm)"]]   # independent variable
y = df["longevity (years)"]  # dependent variable

# Drop rows with missing values
mask = X.notnull().squeeze() & y.notnull()
X = X[mask]
y = y[mask]

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Print results
print("\n📊 Linear Regression Results:")
print("Coefficient (slope):", model.coef_[0])
print("Intercept:", model.intercept_)
print("R² Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
