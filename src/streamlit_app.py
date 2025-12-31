import streamlit as st
import pandas as pd
from dbSetup import get_data
from market_overview import market_overview_tab
from performance import performance_tab
from volatility import volatility_tab
from correlation import correlation_tab
from monthly_performance import monthly_performance_tab
from sector_analysis import sector_analysis_tab

def load_data():
    df = get_data()
    return df

def calculate_daily_returns(df):
    prev_close = df.groupby('Ticker')['close'].shift(1)
    
    df['Daily_Return'] = (df['close'] - prev_close) / prev_close
    
    df['Daily_Return'] = df['Daily_Return'].fillna(0)
    
    print(df)
    return df


def get_yearly_return(df):
    """Calculates total return for each stock"""
    yearly_returns = df.groupby('Ticker').agg(
        Yearly_Return=('close', lambda x: (x.iloc[-1] - x.iloc[0]) / x.iloc[0] if x.iloc[0] != 0 else 0),
        Sector=('Sector', 'first')
    ).reset_index()
        
    return yearly_returns.sort_values(by='Yearly_Return', ascending=False)


def main():
    st.set_page_config(page_title="Stock Performance Dashboard", layout="wide")
    st.title("📊 Nifty 50 Stock Analytics Dashboard")

    try:
        df_raw = load_data()
        df = pd.DataFrame(df_raw)
        df = calculate_daily_returns(df)
        if df.empty:
            st.warning("Database is empty. Please run data_processor.py and dbSetup.py.")
            st.stop()
        st.divider()
        
        yearly_ret = get_yearly_return(df)
        
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📊 Market Overview","🏆 Performance", "📉 Volatility", "🔗 Correlations", "📅 Monthly", "🏭 Sector Analysis"])
        
        with tab1:
            market_overview_tab(df, yearly_ret)
        with tab2:
            performance_tab(yearly_ret)
        with tab3:
            volatility_tab(df, yearly_ret)
        with tab4:
            correlation_tab(df)
        with tab5:
            monthly_performance_tab(df)
        with tab6:
            sector_analysis_tab(yearly_ret)

    except Exception as e:
        st.error(f"Application Error: {e}")

if __name__ == "__main__":
    main()