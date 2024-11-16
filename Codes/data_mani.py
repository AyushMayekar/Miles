import pandas as pd

data = pd.read_csv('data_mani.csv')
df = pd.DataFrame(data)

# Ensure `date` is in datetime format
df["date"] = pd.to_datetime(df["date"])

# Step 1: Group by region and calculate total sales
df["total_sales"] = df["price"] * df["quantity"]
region_sales = df.groupby("region")["total_sales"].sum().reset_index()

# Step 2: Create a new column for average price per unit
df["average_price_per_unit"] = df.groupby("product_id")["price"].transform("mean")

# Step 3: Filter rows where total sales exceed ₹10,000
filtered_df = df[df["total_sales"] > 10000]

# Print Results
print("Grouped by Region (Total Sales):")
print(region_sales)

print("\nData with `average_price_per_unit` Column:")
print(df)

print("\nFiltered Rows (Total Sales > ₹10,000):")
print(filtered_df)
