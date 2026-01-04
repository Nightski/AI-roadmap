import pandas as pd

df = pd.read_csv(r"C:\Users\kevin vinsent\Desktop\kevin\AI-roadmap\Basics\Data_work\Titanic-Dataset.csv")
df['Age'] = df['Age'].fillna(df['Age'].median())
df = df.drop(columns=['Cabin'])
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

#----------------------------------------------------------------------------------------------
#overall surviving rate
#by sex
surv = df.groupby('Sex')['Survived'].mean() * 100
total = round((surv.iloc[0] + surv.iloc[1]) / 2, 2)
print("Female:",round(surv.iloc[0], 2))
print("Male:",round(surv.iloc[1], 2))
print("Total Surviving rate :",total)

#by class
sclass = df.groupby('Pclass')['Survived'].mean() * 100
print("Class 1:",round(sclass.iloc[0],2))
print("Class 2:",round(sclass.iloc[1],2))
print("Class 3:",round(sclass.iloc[2],2))
classtotal = round((sclass.iloc[0] + sclass.iloc[1] + sclass.iloc[2]) / 3, 2)
print("Total Class surviving rate", classtotal)

#avg age of survivors
aage = (df.groupby('Survived')['Age'].mean())
print(aage)

#---------------------------------------------------------------------------------------------
#new columns create
df['Family_size'] = df['SibSp'] + df['Parch'] + 1
df['Isalone'] = (df['Family_size'] == 1).astype(int)

df.to_csv("Titanic_cleaned.csv", index=False)