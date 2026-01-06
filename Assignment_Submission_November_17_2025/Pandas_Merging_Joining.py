import pandas as pd

# 1. Load the dataset

file_path = r"C:\Users\iannr\Training-Submissions\Assignment_Submission_November_17_2025\Sales-Export_2019-2020.csv"
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("-", "_")


print("Dataset Loaded Successfully!\n")
print(df.head())

 
# 2. Create Customer DataFrame

customers = df[['customer_name', 'country']].drop_duplicates()

print("\nCustomers Table")
print(customers.head())


# 3. Create Orders DataFrame

orders = df[['order_id', 'customer_name', 'category', 'order_value_EUR', 'date']]

print("\nOrders Table")
print(orders.head())

 
# 4. Merge customer + order data

merged = pd.merge(
    customers,
    orders,
    on='customer_name',
    how='inner'
)

print("\nMerged Customer + Order Data")
print(merged.head())

# 5. Real Analyst Insight:
# Total orders per customer

customer_order_summary = (
    merged.groupby('customer_name')
          .agg(
              total_orders=('order_id', 'count'),
              total_revenue=('order_value_EUR', 'sum')
          )
          .reset_index()
          .sort_values(by='total_orders', ascending=False)
)

print("\nTotal Orders Per Customer")
print(customer_order_summary.head())


# 6. Save output as CSV (optional)

customer_order_summary.to_csv("customer_order_summary.csv", index=False)
print("\nSummary saved as: customer_order_summary.csv")
