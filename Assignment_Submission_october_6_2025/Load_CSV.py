import pandas as pd

path = "Assignment_Submission_october_6_2025/flowers.csv"

try:
    df = pd.read_csv(path)
    print("First 5 rows of the flowers dataset:")
    print(df.head())
except FileNotFoundError:
    print(f"File not found at {path}. Please check the name and location.")
