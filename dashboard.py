import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\Umar\Documents\10_DA\Excel-Sales-Dashboard\dataset\superstore.csv")

# Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Sales by Category
sales_category = df.groupby("Category")["Sales"].sum()

# Plot chart
sales_category.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.savefig(r"C:\Users\Umar\Documents\10_DA\Excel-Sales-Dashboard\charts\sales_by_category.png")
plt.xticks(rotation=0)
plt.show()