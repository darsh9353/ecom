import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
file_path = "kvg/csekvg.csv"  # Update the path if needed
df = pd.read_csv(file_path)

# Data Cleaning
df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y")  # Convert Date column
df["Amount"] = df["Amount"].replace('[\$,]', '', regex=True).astype(float)  # Convert Amount column

# Visualization 1: Sales Trends Over Time
plt.figure(figsize=(12, 6))
df.groupby("Date")["Amount"].sum().plot(kind="line", marker="o", color="b")
plt.title("Total Sales Over Time", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Sales Amount ($)", fontsize=12)
plt.grid(True)
plt.show()

# Visualization 2: Top-Selling Products
plt.figure(figsize=(12, 6))
top_products = df.groupby("Product")["Amount"].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Best-Selling Products", fontsize=14)
plt.xlabel("Total Sales ($)", fontsize=12)
plt.ylabel("Product", fontsize=12)
plt.show()

# Visualization 3: Sales Distribution by Country
plt.figure(figsize=(12, 6))
sns.boxplot(x="Country", y="Amount", data=df, palette="coolwarm")
plt.title("Sales Distribution by Country", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Sales Amount ($)", fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Visualization 4: Top Salespersons
plt.figure(figsize=(12, 6))
top_salespersons = df.groupby("Sales Person")["Amount"].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_salespersons.values, y=top_salespersons.index, palette="magma")
plt.title("Top 10 Salespersons", fontsize=14)
plt.xlabel("Total Sales ($)", fontsize=12)
plt.ylabel("Sales Person", fontsize=12)
plt.show()
