import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 1. Load Dataset

df = pd.read_csv(r"C:\Users\iannr\Training-Submissions\Assignment_Submission_December_8_2025\StudentsPerformance.csv")
print("Dataset Loaded Successfully!\n")
print(df.head(), "\n")

# 2. Basic Cleaning

# (a) Check missing values
print("Missing values:\n", df.isnull().sum(), "\n")

# (b) Remove duplicates
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print(f"Duplicates removed: {before - after}\n")

# (c) Standardize text columns (lowercase + strip spaces)
text_cols = df.select_dtypes(include="object").columns
for col in text_cols:
    df[col] = df[col].str.lower().str.strip()

print("Text columns standardized.\n")

# 3. Data Type Conversion

# Some datasets store numbers as strings → convert numeric columns
numeric_cols = ["math score", "reading score", "writing score"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("Numeric columns converted.\n")

# 4. OUTLIER DETECTION

# ---- IQR Method ----
def detect_outliers_iqr(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    return df[(df[column] < lower) | (df[column] > upper)]

print("IQR Outliers — Math Score:")
print(detect_outliers_iqr("math score"), "\n")

# ---- Z-SCORE Method ----
df["z_math"] = stats.zscore(df["math score"])
z_outliers = df[df["z_math"].abs() > 3]
print("Z-Score Outliers — Math Score:\n", z_outliers, "\n")

# 5. Visual Outlier Detection

plt.figure(figsize=(8,5))
sns.boxplot(data=df[numeric_cols])
plt.title("Boxplot for Visual Outlier Detection")
plt.savefig("boxplot_outliers.png")
plt.show()

# 6. HANDLING OUTLIERS

# Instead of removing, we cap them using Winsorization
def cap_outliers(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    df[column] = np.where(df[column] < lower, lower,
                 np.where(df[column] > upper, upper, df[column]))

for col in numeric_cols:
    cap_outliers(col)

print("Outliers handled using capping (winsorization).\n")

# 7. Final Summary

print("Final Dataset Info:")
print(df.info(), "\n")

df.to_csv("Cleaned_StudentsPerformance.csv", index=False)
print("Cleaned dataset saved as Cleaned_StudentsPerformance.csv")
