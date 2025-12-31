import streamlit as st
import pandas as pd
import plotly.express as px

def get_monthly_stats(df):
    df_mod = df.copy()
    df_mod['Month'] = df_mod['date'].dt.to_period('M')
    monthly_data = []
    for (month, ticker), group in df_mod.groupby(['Month', 'Ticker']):
        if not group.empty:
            start = group.iloc[0]['close']
            end = group.iloc[-1]['close']
            ret = (end - start) / start if start != 0 else 0
            monthly_data.append({'Month': str(month), 'Ticker': ticker, 'Monthly_Return': ret})
    return pd.DataFrame(monthly_data)

def monthly_performance_tab(df):
    st.subheader("Monthly Breakdown")
    m_df = get_monthly_stats(df)
    sel_month = st.selectbox("Select Month", m_df['Month'].unique())
    f_month = m_df[m_df['Month'] == sel_month].sort_values(by='Monthly_Return', ascending=False)
    c1, c2 = st.columns(2)
    with c1: st.plotly_chart(px.bar(f_month.head(5), x='Ticker', y='Monthly_Return', title="Top 5 Monthly Gainers", color_discrete_sequence=['green']), use_container_width=True)
    with c2: st.plotly_chart(px.bar(f_month.tail(5), x='Ticker', y='Monthly_Return', title="Top 5 Monthly Losers", color_discrete_sequence=['red']), use_container_width=True)