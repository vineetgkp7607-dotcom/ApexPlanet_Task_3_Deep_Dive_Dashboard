import pandas as pd

# Load RFM scored dataset
df = pd.read_csv("reports/rfm_scored.csv")

# Create customer segments based on RFM scores
def segment_customer(row):
    if row["R_Score"] >= 3 and row["F_Score"] >= 3 and row["M_Score"] >= 3:
        return "Champions"
    elif row["R_Score"] >= 3 and row["M_Score"] >= 3:
        return "Potential Loyalists"
    elif row["R_Score"] >= 3:
        return "Recent Customers"
    elif row["R_Score"] <= 2 and row["F_Score"] >= 3:
        return "At Risk"
    else:
        return "Regular Customers"

# Apply segmentation
df["Customer_Segment"] = df.apply(segment_customer, axis=1)

# Count customers in each segment
segment_summary = df["Customer_Segment"].value_counts().reset_index()
segment_summary.columns = ["Customer_Segment", "Customer_Count"]

# Save segmented data
df.to_csv("reports/customer_segments.csv", index=False)
segment_summary.to_csv("reports/segment_summary.csv", index=False)

# Display results
print("=" * 50)
print("       CUSTOMER SEGMENTATION RESULTS")
print("=" * 50)

print("\nCustomer Segment Summary:")
print(segment_summary.to_string(index=False))

print("\nTotal Customers Segmented:", len(df))
print("\nSegmentation completed successfully!")