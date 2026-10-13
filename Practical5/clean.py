import pandas as pd

data = {
    "user": ["Aman", "Riya", "Aman", "Kabir"],
    "text": [
        " AWS is GREAT! ",
        "Good cloud session",
        " AWS is GREAT! ",
        None
    ]
}

df = pd.DataFrame(data)

df = df.drop_duplicates()
df["text"] = df["text"].fillna("")
df["text"] = df["text"].str.strip().str.lower()

print("Cleaned Data:")
print(df)
