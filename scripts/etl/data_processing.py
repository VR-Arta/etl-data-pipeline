import pandas as pd
df = pd.read_csv('data/users.csv')
df['age_group'] = df['age'].apply(lambda x: '18-30' if x < 30 else '30+')
df.to_csv('data/processed_users.csv', index=False)
