import pandas as pd
import numpy as np
import os

# ---------------------------------------------------
# Step 1: Create 'data' folder if it doesn’t exist
# ---------------------------------------------------
os.makedirs("data", exist_ok=True)

# ---------------------------------------------------
# Step 2: Create first file: data.csv
# ---------------------------------------------------
data_df = pd.DataFrame({
    "id": range(1, 11),  # 10 sample IDs
    "review": [
        "Excellent service and friendly staff",
        "Poor experience, will not come again",
        "Average service but good food",
        "Exceptional experience, very satisfied",
        "Bad service, rude behavior",
        "Loved the atmosphere and quality",
        "Not worth the price",
        "Fantastic experience overall",
        "Mediocre service and food",
        "Quick service and polite staff"
    ]
})

# Save data.csv
data_df.to_csv("data/data.csv", index=False)
print("✅ data/data.csv created successfully!")


# ---------------------------------------------------
# Step 3: Create second file: process_data.csv
# (with extra numeric columns)
# ---------------------------------------------------
process_data_df = pd.DataFrame({
    "id": data_df["id"],
    "review": data_df["review"],
    "experience": np.random.randint(1, 10, size=10),
    "service": np.random.randint(1, 10, size=10),
    "quality": np.random.randint(1, 10, size=10)
})

# Save process_data.csv
process_data_df.to_csv("data/process_data.csv", index=False)
print("✅ data/process_data.csv created successfully!")

# ---------------------------------------------------
# Step 4: Display sample output
# ---------------------------------------------------
print("\n📄 data.csv preview:")
print(data_df.head(), "\n")

print("📄 process_data.csv preview:")
print(process_data_df.head())
