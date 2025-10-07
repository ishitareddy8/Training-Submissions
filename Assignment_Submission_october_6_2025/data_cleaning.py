import pandas as pd

# Load dataset
path = "Assignment_Submission_october_6_2025/flowers.csv"
df = pd.read_csv(path)

print("🔹 Original shape:", df.shape)

# 1. Drop completely empty columns (like 'Unnamed: 10')
df = df.dropna(axis=1, how="all")

# 2. Drop duplicate rows
df = df.drop_duplicates()

# 3. Handle missing values:
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        # Fill numeric NaNs with median
        df[col] = df[col].fillna(df[col].median())
    else:
        # Fill non-numeric NaNs with "Unknown"
        df[col] = df[col].fillna("Unknown")

# 4. Clean problematic columns:
# Convert 'height (cm)' to average of range if possible
def convert_height(val):
    if isinstance(val, str) and "-" in val:
        parts = val.split("-")
        try:
            nums = [float(p) for p in parts]
            return sum(nums) / len(nums)
        except:
            return None
    try:
        return float(val)
    except:
        return None

df["height (cm)"] = df["height (cm)"].apply(convert_height)

# Convert 'longevity (years)' to numeric by extracting the first number
def convert_longevity(val):
    if isinstance(val, str):
        # Extract digits at the start
        num = ''.join([c for c in val if c.isdigit()])
        try:
            return int(num)
        except:
            return None
    return val

df["longevity (years)"] = df["longevity (years)"].apply(convert_longevity)

# 5. Save cleaned dataset
cleaned_path = "Assignment_Submission_october_6_2025/flowers_cleaned.csv"
df.to_csv(cleaned_path, index=False)

# 6. Print summary
print("✅ Cleaned shape:", df.shape)
print("\n🔎 Columns:", list(df.columns))
print("\n📊 Summary statistics:")
print(df.describe(include="all"))
print(f"\n✅ Cleaned dataset saved to {cleaned_path}")
