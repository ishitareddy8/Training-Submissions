import pandas as pd
import numpy as np
from scipy import stats
from math import sqrt

# =============================
# CONFIG: update this path only
# =============================
file_path = r"C:\Users\iannr\Training-Submissions\Assignment_Submission_January_5_2026\Sales-Export_2019-2020.csv"

# =============================
# 1) LOAD + CLEAN COLUMN NAMES
# =============================
df = pd.read_csv(file_path)

# Normalize headers to avoid KeyError (spaces, hyphens, hidden chars)
df.columns = (
    df.columns.astype(str)
    .str.strip()
    .str.replace("\ufeff", "", regex=False)   # remove BOM if present
    .str.replace(" ", "_", regex=False)
    .str.replace("-", "_", regex=False)
)

print("✅ Dataset loaded")
print("✅ Columns found:", df.columns.tolist(), "\n")

# =============================
# 2) FIND REVENUE + COST COLUMNS SAFELY
# =============================
def pick_col(possible_names, contains_all=None):
    """Return first matching column from possible_names or by substring rules."""
    for c in possible_names:
        if c in df.columns:
            return c
    if contains_all:
        contains_all = [s.lower() for s in contains_all]
        for c in df.columns:
            cl = c.lower()
            if all(s in cl for s in contains_all):
                return c
    return None

revenue_col = pick_col(
    possible_names=["order_value_EUR", "order_value_eur", "order_value"],
    contains_all=["order", "value"]
)

cost_col = pick_col(
    possible_names=["cost", "Cost"],
    contains_all=["cost"]
)

date_col = pick_col(
    possible_names=["date", "Date"],
    contains_all=["date"]
)

category_col = pick_col(
    possible_names=["category", "Category"],
    contains_all=["category"]
)

device_col = pick_col(
    possible_names=["device_type", "device", "Device_Type"],
    contains_all=["device"]
)

if revenue_col is None:
    raise ValueError("❌ Could not find a revenue column. Check the printed columns list above.")
if cost_col is None:
    raise ValueError("❌ Could not find a cost column. Check the printed columns list above.")

print(f"✅ Using revenue column: {revenue_col}")
print(f"✅ Using cost column: {cost_col}\n")

# Convert revenue/cost to numeric (handles commas)
for col in [revenue_col, cost_col]:
    df[col] = (
        df[col].astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=[revenue_col, cost_col]).copy()

# Parse date if present
if date_col and date_col in df.columns:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df["month"] = df[date_col].dt.to_period("M").astype(str)
else:
    df["month"] = "unknown"

# =============================
# 3) DESCRIPTIVE STATS (CENTRAL TENDENCY + SPREAD)
# =============================
def describe_series(s: pd.Series) -> dict:
    s = s.dropna()
    return {
        "count": int(s.count()),
        "mean": float(s.mean()),
        "median": float(s.median()),
        "mode": float(s.mode().iloc[0]) if not s.mode().empty else np.nan,
        "min": float(s.min()),
        "max": float(s.max()),
        "std_dev": float(s.std(ddof=1)),
        "variance": float(s.var(ddof=1)),
        "IQR": float(s.quantile(0.75) - s.quantile(0.25))
    }

rev_stats = describe_series(df[revenue_col])
cost_stats = describe_series(df[cost_col])

print("===== 📊 DESCRIPTIVE STATS =====")
print("Revenue stats:", rev_stats)
print("Cost stats   :", cost_stats, "\n")

# =============================
# 4) CONFIDENCE INTERVAL (95%) FOR MEAN REVENUE
# =============================
alpha = 0.05
rev = df[revenue_col].dropna()
n = rev.shape[0]
mean = rev.mean()
sd = rev.std(ddof=1)

# t critical value
t_crit = stats.t.ppf(1 - alpha/2, df=n-1)
margin = t_crit * (sd / sqrt(n))
ci_low, ci_high = mean - margin, mean + margin

print("===== ✅ 95% CONFIDENCE INTERVAL (Mean Revenue) =====")
print(f"n = {n}")
print(f"Mean revenue = {mean:,.2f}")
print(f"95% CI       = [{ci_low:,.2f}, {ci_high:,.2f}]\n")

# =============================
# 5) HYPOTHESIS TESTS
#    A) One-sample t-test: mean revenue vs target
#    B) Two-sample t-test (A/B): Mobile vs PC (if device_type exists)
#    C) Chi-square: category vs device (if both exist)
# =============================

# A) One-sample t-test (change target if you want)
TARGET_MEAN = mean  # keep as same mean => p will be ~1; change to a value like 100000 if you want
t_stat, p_val = stats.ttest_1samp(rev, popmean=TARGET_MEAN)

print("===== 🧪 ONE-SAMPLE T-TEST =====")
print(f"H0: mean(revenue) = {TARGET_MEAN:,.2f}")
print(f"t-stat = {t_stat:.4f}, p-value = {p_val:.6f}")
print("Decision (alpha=0.05):", "Reject H0" if p_val < 0.05 else "Fail to reject H0", "\n")

# B) Two-sample t-test (A/B): Mobile vs PC (or any two devices)
print("===== 🧪 TWO-SAMPLE T-TEST (A/B) =====")
if device_col and device_col in df.columns:
    dfx = df.dropna(subset=[device_col, revenue_col]).copy()
    dfx[device_col] = dfx[device_col].astype(str).str.strip().str.lower()

    group_a_name = "mobile"
    group_b_name = "pc"

    A = dfx.loc[dfx[device_col] == group_a_name, revenue_col].dropna()
    B = dfx.loc[dfx[device_col] == group_b_name, revenue_col].dropna()

    if len(A) >= 5 and len(B) >= 5:
        # Welch’s t-test (unequal variances)
        t2, p2 = stats.ttest_ind(A, B, equal_var=False)
        print(f"Groups: A={group_a_name} (n={len(A)}), B={group_b_name} (n={len(B)})")
        print(f"Mean(A)={A.mean():,.2f}, Mean(B)={B.mean():,.2f}")
        print(f"t-stat = {t2:.4f}, p-value = {p2:.6f}")
        print("Decision (alpha=0.05):", "Reject H0" if p2 < 0.05 else "Fail to reject H0", "\n")
    else:
        print("Not enough rows for Mobile vs PC t-test. (Need at least 5 rows per group)\n")
else:
    print("device_type column not found -> skipping A/B t-test.\n")

# C) Chi-square test of independence: category vs device_type
print("===== 🧪 CHI-SQUARE TEST (Independence) =====")
if category_col and device_col and category_col in df.columns and device_col in df.columns:
    dfx = df.dropna(subset=[category_col, device_col]).copy()
    dfx[category_col] = dfx[category_col].astype(str).str.strip().str.lower()
    dfx[device_col] = dfx[device_col].astype(str).str.strip().str.lower()

    contingency = pd.crosstab(dfx[category_col], dfx[device_col])

    if contingency.shape[0] > 1 and contingency.shape[1] > 1:
        chi2, p_chi, dof, expected = stats.chi2_contingency(contingency)
        print("Contingency table shape:", contingency.shape)
        print(f"chi2 = {chi2:.4f}, dof = {dof}, p-value = {p_chi:.6f}")
        print("Decision (alpha=0.05):", "Reject H0 (dependent)" if p_chi < 0.05 else "Fail to reject H0 (independent)")
    else:
        print("Not enough categories/devices for chi-square test.")
else:
    print("category/device columns not found -> skipping chi-square test.")

print("\n✅ Week 11 statistical analysis completed successfully.")
