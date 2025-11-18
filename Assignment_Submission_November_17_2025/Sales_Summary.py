import pandas as pd

# Load dataset with full path
df = pd.read_csv(r"C:\Users\iannr\Training-Submissions\Assignment_Submission_November_17_2025\Sales-Export_2019-2020.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert values to numbers
df["order_value_EUR"] = df["order_value_EUR"].str.replace(",", "").astype(float)
df["cost"] = df["cost"].astype(float)

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Extract month & year
df["month"] = df["date"].dt.to_period("M")

# Create sales summary
sales_summary = df.groupby(["category", "month"])["order_value_EUR"].sum().reset_index()

# Save output
output_path = r"C:\Users\iannr\Training-Submissions\Assignment_Submission_November_17_2025\sales_summary_by_category_month.csv"
sales_summary.to_csv(output_path, index=False)

print("Sales Summary Saved At:")
print(output_path)
