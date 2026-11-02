import pandas as pd

# Load dataset
df = pd.read_csv("data/sales_cleaned.csv")

# Calculate KPIs
total_revenue = df["Total_Sales"].sum()
total_orders = df["Order_ID"].nunique()
average_order_value = total_revenue / total_orders
total_customers = df["Customer_ID"].nunique()
average_quantity = df["Quantity"].sum() / total_orders

# Display results
print("=" * 45)
print("       SALES PERFORMANCE KPIs")
print("=" * 45)

print(f"Total Revenue: Rs. {total_revenue:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: Rs. {average_order_value:,.2f}")
print(f"Total Customers: {total_customers:,}")
print(f"Average Quantity per Order: {average_quantity:.2f}")

print("=" * 45)