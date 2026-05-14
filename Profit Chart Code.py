import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# CREATE CHARTS FOLDER
# =========================
os.makedirs(
    r"C:\Users\Umar\Documents\10_DA\Excel-Sales-Dashboard\charts",
    exist_ok=True
)

# =========================
# LOAD DATASET
# =========================
df = pd.read_csv(
    r"C:\Users\Umar\Documents\10_DA\Excel-Sales-Dashboard\dataset\superstore.csv"
)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# =========================
# CONVERT DATE
# =========================
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed"
)

# Create Month column
df["Month"] = df["Order Date"].dt.strftime("%b %Y")

# =========================
# TOTAL SALES
# =========================
total_sales = df["Sales"].sum()

# =========================
# TOTAL ORDERS
# =========================
total_orders = df["Order ID"].nunique()

print("================================")
print("TOTAL SALES:", round(total_sales, 2))
print("TOTAL ORDERS:", total_orders)
print("================================")

# ==================================================
# CHART 1 — SALES BY CATEGORY (BAR CHART)
# ==================================================
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Horizontal labels
plt.xticks(rotation=0)

# Save chart
plt.savefig(
    r"C:\Users\Umar\Documents\10_DA\Excel-Sales-Dashboard\charts\sales_by_category.png"
)

plt.show()

# ==================================================
# CHART 2 — CATEGORY DISTRIBUTION (PIE CHART)
# ==================================================
plt.figure(figsize=(7,7))

category_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Category Distribution")

# Remove y-axis label
plt.ylabel("")

# Save chart
plt.savefig(
    r"C:\Users\Umar\Documents\10_DA\Excel-Sales-Dashboard\charts\category_distribution.png"
)

plt.show()

# ==================================================
# CHART 3 — MONTHLY SALES TREND (LINE CHART)
# ==================================================
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12,5))

monthly_sales.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Horizontal labels
plt.xticks(rotation=0)

# Save chart
plt.savefig(
    r"C:\Users\Umar\Documents\10_DA\Excel-Sales-Dashboard\charts\monthly_sales_trend.png"
)

plt.show()

print("================================")
print("Charts Saved Successfully!")
print("================================")