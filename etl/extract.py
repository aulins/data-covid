import requests
import json

url = 'https://disease.sh/v3/covid-19/countries'
response = requests.get(url)
data = response.json()

with open('data/raw/covid_data_raw.json', 'w') as f:
    json.dump(data, f, indent=4)
