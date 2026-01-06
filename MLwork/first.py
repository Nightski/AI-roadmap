import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
pd.set_option('future.no_silent_downcasting', True)

df = pd.read_csv(r"C:\Users\kevin vinsent\Desktop\kevin\AI-roadmap\Basics\Data_work\Titanic_cleaned.csv")
features = [
    'Pclass',
    'Sex',
    'Age',
    'Family_size',
    'Isalone'
]
target = 'Survived'
maping = {"male":1,"female":0}
df['Sex'] = df['Sex'].replace(maping).infer_objects(copy=False)

x = df[features]
y = df[target]

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.3,random_state=42)

#Logistic regression
model = LogisticRegression(max_iter=1000)
model.fit(xtrain, ytrain)
#Decision tree
tree = DecisionTreeClassifier(max_depth=5,random_state=43)
tree.fit(xtrain,ytrain)

ypred = model.predict(xtest)
print("Acc: ", accuracy_score(ytest, ypred) * 100)
print(classification_report(ytest, ypred))

tree_pred = tree.predict(xtest)
print("ACC of tree: ",accuracy_score(ytest,tree_pred) * 100)

#which one was better
comparison = pd.DataFrame({
    "Model": ["Logistic Regression", "Decision Tree"],
    "Accuracy": [
        accuracy_score(ytest, ypred) * 100,
        accuracy_score(ytest, tree_pred) * 100
    ]
})

print(comparison)