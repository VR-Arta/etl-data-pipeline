import pandas as pd
from datetime import datetime
def process_dates(file):
    df = pd.read_csv(file)
    df['processed_date'] = datetime.now().strftime('%Y-%m-%d')
    df.to_csv('data/processed_dates.csv', index=False)
process_dates('data/raw_dates.csv')
