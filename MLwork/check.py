import pandas as pd

df = pd.read_csv(r"C:\Users\kevin vinsent\Downloads\my_file.csv")
print(df.info())

df = df.drop_duplicates()
df = df.dropna(how="all")

numeric = df.select_dtypes(include=["int64", "float32", "float64"]).columns
for col in numeric:
    df[col] = df[col].fillna(df[col].median())

text_col = df.select_dtypes(include=["object","string"]).columns
for col in text_col:
    df[col] = df[col].fillna("Unknown")

for cl in text_col:
    df[cl] = df[cl].str.strip().str.lower()

if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'],errors="coerce")

for col in numeric:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    df = df[(df[col] >= q1 - 1.5*iqr) & (df[col] <= q3 + 1.5*iqr)]

df.to_csv("Modified", index=False)
print("Completed Successfully")