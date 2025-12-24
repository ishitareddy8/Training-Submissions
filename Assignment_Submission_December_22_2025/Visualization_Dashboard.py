import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. LOAD DATASET
# -----------------------------
file_path = "C:/Users/iannr/Training-Submissions/Assignment_Submission_December_22_2025/Sales-Export_2019-2020.csv"
df = pd.read_csv(file_path)

print("Dataset Loaded Successfully")
print(df.head(), "\n")

# Clean column names (IMPORTANT)
df.columns = df.columns.str.strip()

# Fix numeric column with commas
df["order_value_EUR"] = (
    df["order_value_EUR"]
    .astype(str)
    .str.replace(",", "", regex=True)
    .astype(float)
)

# Convert date column
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

# -----------------------------
# 2. MULTI-PLOT DASHBOARD
# -----------------------------
plt.figure(figsize=(14, 10))

# Plot 1: Line Chart – Monthly Revenue Trend
plt.subplot(2, 2, 1)
monthly_sales = df.groupby("month")["order_value_EUR"].sum()
monthly_sales.plot(marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (EUR)")
plt.xticks(rotation=45)

# Plot 2: Bar Chart – Revenue by Category
plt.subplot(2, 2, 2)
category_sales = df.groupby("category")["order_value_EUR"].sum().sort_values()
category_sales.plot(kind="barh", color="teal")
plt.title("Revenue by Product Category")
plt.xlabel("Revenue (EUR)")

# Plot 3: Scatter Plot – Cost vs Revenue
plt.subplot(2, 2, 3)
plt.scatter(df["cost"], df["order_value_EUR"], alpha=0.6)
plt.title("Cost vs Order Value")
plt.xlabel("Cost")
plt.ylabel("Order Value")

# Plot 4: Histogram – Distribution of Order Value
plt.subplot(2, 2, 4)
plt.hist(df["order_value_EUR"], bins=30, color="purple", alpha=0.7)
plt.title("Distribution of Order Value")
plt.xlabel("Order Value")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("multi_plot_dashboard.png")
plt.show()

# -----------------------------
# 3. SALES PERFORMANCE DASHBOARD (4 CHART TYPES)
# -----------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Chart 1: Line – Monthly Sales
sns.lineplot(
    x=monthly_sales.index,
    y=monthly_sales.values,
    ax=axes[0, 0],
    marker="o"
)
axes[0, 0].set_title("Monthly Sales Performance")
axes[0, 0].tick_params(axis="x", rotation=45)

# Chart 2: Bar – Country Revenue
country_sales = df.groupby("country")["order_value_EUR"].sum().sort_values()
sns.barplot(
    x=country_sales.values,
    y=country_sales.index,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Revenue by Country")

# Chart 3: Pie – Device Type Share
device_sales = df.groupby("device_type")["order_value_EUR"].sum()
axes[1, 0].pie(
    device_sales,
    labels=device_sales.index,
    autopct="%1.1f%%",
    startangle=140
)
axes[1, 0].set_title("Sales by Device Type")

# Chart 4: Heatmap – Category vs Month
pivot_table = pd.pivot_table(
    df,
    values="order_value_EUR",
    index="category",
    columns="month",
    aggfunc="sum"
)

sns.heatmap(
    pivot_table,
    cmap="Blues",
    ax=axes[1, 1]
)
axes[1, 1].set_title("Sales Heatmap (Category vs Month)")

plt.tight_layout()
plt.savefig("sales_performance_dashboard.png")
plt.show()

print("Dashboards generated successfully!")
