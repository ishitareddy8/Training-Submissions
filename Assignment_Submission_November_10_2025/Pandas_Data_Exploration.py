import pandas as pd
from sklearn.datasets import load_iris

# 1. Load Dataset into a DataFrame

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# 2. DataFrame Anatomy & Basic Inspection

print("First 10 Rows of the Dataset")
print(df.head(10), "\n")

print("DataFrame Info")
print(df.info(), "\n")

print("Summary Statistics")
print(df.describe(), "\n")

# 3. Boolean Indexing (Filtering Examples)

print(" Filter: Only Setosa Flowers")
print(df[df['species'] == 'setosa'].head(), "\n")

print("Filter: Petal Length > 5.0 cm")
print(df[df['petal length (cm)'] > 5.0].head(), "\n")

# 4. Missing Values Check

print(" Missing Values Count")
print(df.isnull().sum(), "\n")

# 5. Unique Categories and Value Counts

print("Unique Species")
print(df['species'].unique(), "\n")

print("Species Distribution")
print(df['species'].value_counts(), "\n")

# 6. Grouped Averages (Mean per Species)

print("Average Measurements Grouped by Species")
print(df.groupby('species').mean(), "\n")
