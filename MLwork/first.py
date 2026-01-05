import pandas as pd
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