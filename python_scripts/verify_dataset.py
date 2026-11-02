import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/sales_cleaned.csv")

# Display basic information
print("DATASET LOADED SUCCESSFULLY")
print("-" * 40)

print("Rows and Columns:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())