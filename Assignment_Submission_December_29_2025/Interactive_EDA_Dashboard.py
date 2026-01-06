import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# 1. LOAD DATA
# -----------------------------
file_path = r"C:\Users\iannr\Training-Submissions\Assignment_Submission_December_29_2025\Sales-Export_2019-2020.csv"
df = pd.read_csv(file_path)

# Clean column names (fix hidden spaces)
df.columns = df.columns.str.strip()

print("Dataset loaded successfully")
print(df.head(), "\n")
print("Columns:", df.columns.tolist(), "\n")

# -----------------------------
# 2. FIND REVENUE COLUMN SAFELY
# -----------------------------
revenue_candidates = [c for c in df.columns if "order" in c.lower() and "eur" in c.lower()]
if not revenue_candidates:
    raise KeyError(f"Could not find revenue column. Available columns: {df.columns.tolist()}")

revenue_col = revenue_candidates[0]
print("Using revenue column:", revenue_col, "\n")

# -----------------------------
# 3. CLEAN REQUIRED COLUMNS
# -----------------------------
df[revenue_col] = (
    df[revenue_col]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.strip()
)

df[revenue_col] = pd.to_numeric(df[revenue_col], errors="coerce")

if "cost" in df.columns:
    df["cost"] = (
        df["cost"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df["cost"] = pd.to_numeric(df["cost"], errors="coerce")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date", revenue_col])

df["month"] = df["date"].dt.to_period("M").astype(str)

# -----------------------------
# 4. UNIVARIATE ANALYSIS
# -----------------------------
fig_hist = px.histogram(
    df,
    x=revenue_col,
    nbins=40,
    title="Distribution of Order Value (EUR)",
)
fig_hist.show()

# -----------------------------
# 5. BIVARIATE ANALYSIS
# -----------------------------
if "cost" in df.columns and "category" in df.columns:
    fig_scatter = px.scatter(
        df,
        x="cost",
        y=revenue_col,
        color="category",
        title="Cost vs Order Value by Product Category",
        hover_data=["country", "device_type"] if "country" in df.columns and "device_type" in df.columns else None
    )
    fig_scatter.show()

# -----------------------------
# 6. MULTIVARIATE ANALYSIS
# -----------------------------
if "category" in df.columns:
    category_month_sales = (
        df.groupby(["month", "category"])[revenue_col]
        .sum()
        .reset_index()
    )

    fig_line = px.line(
        category_month_sales,
        x="month",
        y=revenue_col,
        color="category",
        title="Monthly Revenue Trend by Category"
    )
    fig_line.show()

# -----------------------------
# 7. INTERACTIVE FILTER DASHBOARD (Country Dropdown)
# -----------------------------
if "country" in df.columns and "cost" in df.columns:
    countries = sorted(df["country"].dropna().unique().tolist())

    traces = []
    for c in countries:
        temp = df[df["country"] == c]
        traces.append(
            go.Scatter(
                x=temp["cost"],
                y=temp[revenue_col],
                mode="markers",
                name=c,
                visible=True if c == countries[0] else False
            )
        )

    dropdown_buttons = []
    for i, c in enumerate(countries):
        visibility = [False] * len(countries)
        visibility[i] = True
        dropdown_buttons.append(
            dict(
                label=c,
                method="update",
                args=[{"visible": visibility}, {"title": f"Interactive Sales Explorer – {c}"}]
            )
        )

    fig_filter = go.Figure(data=traces)
    fig_filter.update_layout(
        title=f"Interactive Sales Explorer – {countries[0]}",
        xaxis_title="Cost (EUR)",
        yaxis_title="Order Value (EUR)",
        updatemenus=[dict(buttons=dropdown_buttons, direction="down", x=1.15, y=1)]
    )
    fig_filter.show()

# -----------------------------
# 8. CORRELATION HEATMAP
# -----------------------------
if "cost" in df.columns:
    numeric_df = df[[revenue_col, "cost"]].dropna()
    corr = numeric_df.corr()

    fig_corr = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Heatmap (Cost vs Revenue)",
        color_continuous_scale="Blues"
    )
    fig_corr.show()

# -----------------------------
# 9. BUSINESS INSIGHTS SUMMARY
# -----------------------------
print("\nKEY INSIGHTS:")
print("- Revenue varies significantly across product categories and months.")
print("- Cost and revenue show a positive relationship in most cases.")
print("- Some countries contribute more strongly to total revenue than others.")
print("- Device type and category patterns can be explored using interactive charts.")

print("\nInteractive EDA dashboard completed successfully ✅")
