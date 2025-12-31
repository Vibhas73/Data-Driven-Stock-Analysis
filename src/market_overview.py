import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def market_overview_tab(df, yearly_ret):
    total_stocks = len(yearly_ret)
    green_stocks = len(yearly_ret[yearly_ret['Yearly_Return'] > 0])
    red_stocks = len(yearly_ret[yearly_ret['Yearly_Return'] <= 0])

    col1, col2= st.columns([2,1],border=True)

    with col1:
            st.subheader("📊 Market Overview")
            n1, n2, n3 = st.columns(3)
            with n1:
                st.metric("📶 Total Stocks", total_stocks)
            with n2:
                st.metric("📈 Green Stocks", green_stocks, delta_color="normal" )
            with n3:
                st.metric("📉 Red Stocks",  red_stocks, delta_color="inverse")

            st.divider()

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Average Price", f"₹{df['close'].mean():.0f}")
            avg_vol_million = df['volume'].mean() / 1_000_000
            m2.metric("Average Volume", f"{avg_vol_million:.1f}M")
            m3.metric("Best Performer", yearly_ret.iloc[0]['Ticker'], f"{yearly_ret.iloc[0]['Yearly_Return']:.2%}")
            m4.metric("Worst Performer", yearly_ret.iloc[-1]['Ticker'], f"{yearly_ret.iloc[-1]['Yearly_Return']:.2%}")

    with col2:
        labels = ['Green', 'Red']
        values = [green_stocks, red_stocks]
        colors = ['#2ecc71', '#e74c3c']

        fig, ax = plt.subplots()
        ax.pie(
                values,
                labels=['', ''],         # hide side labels
                autopct='%1.0f%%',       # show % inside chart
                colors=colors,
                startangle=90,
                textprops={'color': 'white', 'fontsize': 16}
            )
            
        ax.text(-1.5, 0, "Green", color='#2ecc71', fontsize=14, fontweight='bold')
        ax.text(1.0, 0, "Red", color='#e74c3c', fontsize=14, fontweight='bold')
        st.subheader("Green vs Red Stocks")
        st.pyplot(fig)
