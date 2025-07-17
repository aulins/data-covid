import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine("postgresql://postgres:bismillah@localhost:5432/covid_data")

df = pd.read_csv('data/cleaned/covid_cleaned.csv')
df.to_sql("covid_stats", con=engine, if_exists='replace', index=False)
