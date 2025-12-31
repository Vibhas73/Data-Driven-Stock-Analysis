import os
import yaml
import pandas as pd

# Updated Nifty 50 Sector Mapping based on your dataset
NIFTY_SECTORS = {
    'SBIN': 'Financial Services',
    'BAJFINANCE': 'Financial Services',
    'TITAN': 'Consumer Durables',
    'ITC': 'FMCG',
    'TCS': 'IT',
    'LT': 'Construction',
    'TATACONSUM': 'FMCG',
    'RELIANCE': 'Oil & Gas',
    'HCLTECH': 'IT',
    'JSWSTEEL': 'Metals',
    'ULTRACEMCO': 'Construction Materials',
    'POWERGRID': 'Power',
    'INFY': 'IT',
    'TRENT': 'Retail',
    'BHARTIARTL': 'Telecom',
    'TATAMOTORS': 'Automobile',
    'WIPRO': 'IT',
    'TECHM': 'IT',
    'NTPC': 'Power',
    'HINDUNILVR': 'FMCG',  # Note: HUL is often listed as HINDUNILVR in data
    'APOLLOHOSP': 'Healthcare',
    'M&M': 'Automobile',
    'GRASIM': 'Construction Materials',
    'ICICIBANK': 'Financial Services',
    'ADANIENT': 'Metals & Mining',
    'ADANIPORTS': 'Services',
    'BEL': 'Defense',
    'BAJAJFINSV': 'Financial Services',
    'EICHERMOT': 'Automobile',
    'COALINDIA': 'Metals & Mining',
    'MARUTI': 'Automobile',
    'INDUSINDBK': 'Financial Services',
    'ASIANPAINT': 'Consumer Durables',
    'TATASTEEL': 'Metals',
    'HDFCLIFE': 'Financial Services',
    'DRREDDY': 'Healthcare',
    'SUNPHARMA': 'Healthcare',
    'KOTAKBANK': 'Financial Services',
    'SHRIRAMFIN': 'Financial Services',
    'NESTLEIND': 'FMCG',
    'ONGC': 'Oil & Gas',
    'CIPLA': 'Healthcare',
    'BPCL': 'Oil & Gas',
    'BRITANNIA': 'FMCG',
    'SBILIFE': 'Financial Services',
    'HINDALCO': 'Metals',
    'HEROMOTOCO': 'Automobile',
    'AXISBANK': 'Financial Services',
    'HDFCBANK': 'Financial Services',
    'BAJAJ-AUTO': 'Automobile'
}


def extract_from_yaml():
    RAW_PATH = "../data_raw"
    OUTPUT = "../data_processed"
    os.makedirs(OUTPUT, exist_ok=True)
    stock_data = {}

    for month in os.listdir(RAW_PATH):
        month_path = os.path.join(RAW_PATH, month)
        for file in os.listdir(month_path):
            if file.endswith(('.yaml', '.yml')):
                with open(os.path.join(month_path, file)) as f:
                    data = yaml.safe_load(f)
                    for record in data:
                        ticker = record['Ticker']
                        if ticker not in stock_data:
                            stock_data[ticker] = []
                        stock_data[ticker].append(record)

    for ticker, records in stock_data.items():
        df = pd.DataFrame(records)
        df['Sector'] = df['Ticker'].map(NIFTY_SECTORS).fillna('Others')
        df.to_csv(f"{OUTPUT}/{ticker}.csv", index=False)
    print("CSV Created Successfully!")
    return df 

if __name__ == "__main__":
    extract_from_yaml()
