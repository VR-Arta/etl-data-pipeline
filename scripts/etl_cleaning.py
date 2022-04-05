import pandas as pd

df = pd.read_csv('data/raw_data.csv')
df.dropna(inplace=True)
df.to_csv('data/clean_data.csv', index=False)
print('Data cleaned and saved')
