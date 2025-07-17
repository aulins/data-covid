import json
import pandas as pd

with open('data/raw/covid_data_raw.json') as f:
    data = json.load(f)

df = pd.json_normalize(data)
df = df[['country', 'cases', 'deaths', 'recovered']]
df.to_csv('data/cleaned/covid_cleaned.csv', index=False)
