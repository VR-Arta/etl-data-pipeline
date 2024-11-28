import pandas as pd
def process_transactions(file):
    df = pd.read_csv(file)
    df['amount'] = df['amount'].apply(lambda x: round(x, 2))
    df.to_csv('data/cleaned_transactions.csv', index=False)
process_transactions('data/raw_transactions.csv')
