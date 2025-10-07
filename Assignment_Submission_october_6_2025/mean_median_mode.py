import pandas as pd

path = "Assignment_Submission_october_6_2025/flowers.csv"

try:
    df = pd.read_csv(path)

    column = "number"

    if column not in df.columns:
        print(f"Column '{column}' not found in the dataset. Available columns: {list(df.columns)}")
    else:
        s = df[column].dropna()
        print(f"Mean   of {column}: {s.mean()}")
        print(f"Median of {column}: {s.median()}")
        print(f"Mode   of {column}: {s.mode().tolist()}")
except FileNotFoundError:
    print(f"File {path} not found. Make sure your CSV is inside the assignment folder.")
