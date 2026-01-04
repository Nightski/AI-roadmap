import pandas as pd
pd.set_option('future.no_silent_downcasting', True)

df = pd.read_csv(r"C:\Users\kevin vinsent\Desktop\kevin\AI-roadmap\Basics\Data_work\Titanic-Dataset.csv")
change = {"male" : 1, "female" : 0}

df['Sex'] = df['Sex'].replace(change).infer_objects(copy=False)

#how many dead count
dead = df['Survived'].value_counts()

#chance of surviving based on sex
grp = df.groupby('Sex')['Survived'].mean() * 100

#cleaning null data
print(df.isnull().sum())
df = df.drop(columns=['Cabin'])
print(df.isnull().sum())