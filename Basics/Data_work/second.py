import pandas as pd
pd.set_option('future.no_silent_downcasting', True)

df = pd.read_csv(r"C:\Users\kevin vinsent\Downloads\house_prices.csv")
df['date'] = pd.to_datetime(df['date'],format="%Y%m%dT%H%M%S").dt.normalize()

features = [
    'bedrooms',
    'floors',
    'bathrooms',
    'waterfront'
    'condition'
]
df['waterfront'] = df['waterfront'].replace({"N":0, "Y":1}).infer_objects(copy=False).astype(int)
print(df['condition'].unique())
cond = {'Average': 2 ,'Very Good' : 4, 'Good' : 3, 'Poor': 0, 'Fair' : 1}
df['condition'] = df['condition'].replace(cond).infer_objects(copy=False).astype(int)
