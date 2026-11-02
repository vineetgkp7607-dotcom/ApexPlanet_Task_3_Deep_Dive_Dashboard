import pandas as pd

# Load RFM dataset
df = pd.read_csv("data/rfm_analysis.csv")

# Convert date column
df["Last_Order_Date"] = pd.to_datetime(
    df["Last_Order_Date"], dayfirst=True
)

# Calculate RFM scores
# Lower Recency is better
df["R_Score"] = pd.qcut(
    df["Recency"].rank(method="first"),
    4,
    labels=[4, 3, 2, 1]
).astype(int)

# Higher Frequency is better
df["F_Score"] = df["Frequency"].map({
    1: 1,
    2: 3,
    3: 4
}).astype(int)

# Higher Monetary is better
df["M_Score"] = pd.qcut(
    df["Monetary"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
).astype(int)

# Calculate combined RFM score
df["RFM_Score"] = (
    df["R_Score"] +
    df["F_Score"] +
    df["M_Score"]
)

# Save RFM analysis results
df.to_csv("reports/rfm_scored.csv", index=False)

# Display results
print("=" * 50)
print("          RFM CUSTOMER ANALYSIS")
print("=" * 50)

print("\nFirst 10 Customer Records:")
print(df.head(10).to_string(index=False))

print("\nRFM Score Summary:")
print(df[["R_Score", "F_Score", "M_Score"]].describe())

print("\nTotal Customers Analyzed:", len(df))
print("\nRFM analysis completed successfully!")
print("Output saved: reports/rfm_scored.csv")
