import pandas as pd

df = pd.read_csv(r"C:\Users\kevin vinsent\Desktop\kevin\AI-roadmap\Basics\Data_work\Titanic-Dataset.csv")
change = {"male" : 1, "female" : 0}
print(df.columns)
df = df['Sex'].replace(change).infer_objects(copy=False)
print(df.head(3))