import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
pd.set_option('future.no_silent_downcasting', True)

df = pd.read_csv(r"C:\Users\kevin vinsent\Downloads\house_prices.csv")
df['date'] = pd.to_datetime(df['date'],format="%Y%m%dT%H%M%S").dt.normalize()

df['was_renovated'] = (df['yr_renovated'] != 0).astype(int)
df['reno_age'] = 0
df.loc[df['yr_renovated'] != 0, 'reno_age'] = (
    df['date'].dt.year - df['yr_renovated']
)

df['waterfront'] = df['waterfront'].replace({"N":0, "Y":1}).infer_objects(copy=False).astype(int)

cond = {'Average': 2 ,'Very Good' : 4, 'Good' : 3, 'Poor': 0, 'Fair' : 1}
df['condition'] = df['condition'].replace(cond).infer_objects(copy=False).astype(int)

df['floors'] = df['floors'].astype(int)

features = [
    'bedrooms',
    'floors',
    'bathrooms',
    'waterfront',
    'condition'
]

x = df[features]
y = df['price']
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2,random_state=42)
model = DecisionTreeRegressor(max_depth=5,random_state=42)
model.fit(xtrain, ytrain)
ypred = model.predict(xtest)
print("R2", r2_score(ytest, ypred))
print("MAE",mean_absolute_error(ytest, ypred))