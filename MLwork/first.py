import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
pd.set_option('future.no_silent_downcasting', True)

df = pd.read_csv(r"C:\Users\kevin vinsent\Desktop\kevin\AI-roadmap\Basics\Data_work\Titanic_cleaned.csv")
features = {
    'Pclass',
    'Sex',
    'Age',
    'Family_size',
    'Isalone'
}
target = 'Survived'
maping = {"male":1,"female":0}
df['Sex'] = df['Sex'].replace(maping).infer_objects(copy=False)

x = df[features]
y = df[target]

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.3,random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(xtrain, ytrain)

