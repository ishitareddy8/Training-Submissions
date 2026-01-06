import pandas as pd
import numpy as np
from scipy import stats
import os

# -------------------------------------------------
# CONFIGURATION
# -------------------------------------------------

BASE_DIR = r"C:\Users\iannr\Training-Submissions\Assignment_Submission_December_15_2025"
INPUT_FILE = os.path.join(BASE_DIR, "StudentsPerformance.csv")

CLEANED_FILE = os.path.join(BASE_DIR, "Cleaned_StudentsPerformance.csv")
QUALITY_CSV = os.path.join(BASE_DIR, "data_quality_report.csv")
QUALITY_TXT = os.path.join(BASE_DIR, "Data_quality_report.txt")
ANOMALY_FILE = os.path.join(BASE_DIR, "anomaly_records.csv")

# -------------------------------------------------
# 1. EXTRACT – Load Data
# -------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("Dataset loaded successfully\n")
print(df.head(), "\n")

# -------------------------------------------------
# 2. DATA QUALITY ASSESSMENT
# -------------------------------------------------

quality_report = pd.DataFrame({
    "Column": df.columns,
    "Missing_Values": df.isnull().sum(),
    "Duplicate_Values": df.duplicated().sum(),
    "Data_Type": df.dtypes.values
})

quality_report.to_csv(QUALITY_CSV, index=False)
print("Data quality CSV report generated\n")

# -------------------------------------------------
# 3. AUTOMATED DATA CLEANING
# -------------------------------------------------

# Remove duplicates
df = df.drop_duplicates()

# Standardize text columns
text_cols = df.select_dtypes(include="object").columns
for col in text_cols:
    df[col] = df[col].str.lower().str.strip()

# Convert numeric columns
numeric_cols = ["math score", "reading score", "writing score"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Handle missing numeric values
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

print("Automated data cleaning completed\n")

# -------------------------------------------------
# 4. ANOMALY / OUTLIER DETECTION (IQR)
# -------------------------------------------------

def detect_iqr_outliers(dataframe, column):
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return dataframe[(dataframe[column] < lower) | (dataframe[column] > upper)]

outliers = pd.concat(
    [detect_iqr_outliers(df, col) for col in numeric_cols]
).drop_duplicates()

outliers.to_csv(ANOMALY_FILE, index=False)
print("Anomaly records saved\n")

# -------------------------------------------------
# 5. OUTLIER HANDLING – WINSORIZATION
# -------------------------------------------------

def winsorize_column(dataframe, column):
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    dataframe[column] = np.where(
        dataframe[column] < lower, lower,
        np.where(dataframe[column] > upper, upper, dataframe[column])
    )

for col in numeric_cols:
    winsorize_column(df, col)

print("Outliers handled using winsorization\n")

# -------------------------------------------------
# 6. LOAD – Save Cleaned Dataset
# -------------------------------------------------

df.to_csv(CLEANED_FILE, index=False)
print("Cleaned dataset saved successfully\n")

# -------------------------------------------------
# 7. DATA QUALITY TEXT REPORT
# -------------------------------------------------

with open(QUALITY_TXT, "w") as f:
    f.write("DATA QUALITY REPORT\n")
    f.write("===================\n\n")

    f.write(f"Dataset Shape:\nRows: {df.shape[0]}, Columns: {df.shape[1]}\n\n")

    f.write("Missing Values:\n")
    f.write(str(df.isnull().sum()))
    f.write("\n\n")

    f.write("Duplicate Rows:\n")
    f.write(str(df.duplicated().sum()))
    f.write("\n\n")

    f.write("Column Data Types:\n")
    f.write(str(df.dtypes))
    f.write("\n")

print("Data quality report saved as Data_quality_report.txt\n")

# -------------------------------------------------
# FINAL SUMMARY
# -------------------------------------------------

print("Final Dataset Info:\n")
print(df.info())
