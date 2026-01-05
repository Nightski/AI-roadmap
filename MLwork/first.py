import pandas as pd

df = pd.read_csv(r"C:\Users\kevin vinsent\Desktop\kevin\AI-roadmap\Basics\Data_work\Titanic_cleaned.csv")
features = {
    'Pclass',
    'Sex',
    'Age',
    'Family_size',
    'Isalone'
}
target = 'Survived'