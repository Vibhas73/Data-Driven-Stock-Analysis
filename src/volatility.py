import streamlit as st
import pandas as pd
import plotly.express as px

def get_volatility(df):
    """Calculates Risk"""
    volatility = df.groupby('Ticker')['Daily_Return'].std().reset_index()
    volatility.columns = ['Ticker', 'Volatility']
    return volatility.sort_values(by='Volatility', ascending=False)

def get_cumulative_returns(df, top_n_tickers):
    df = df.sort_values('date')
    subset = df[df['Ticker'].isin(top_n_tickers)].copy()
    subset['Cumulative_Return'] = subset.groupby('Ticker')['Daily_Return'].transform(lambda x: (1 + x).cumprod() - 1)
    return subset

def volatility_tab(df, yearly_ret):
    c1, c2 = st.columns([1, 2])
    vol_df = get_volatility(df)
    vol_df = vol_df.reset_index(drop=True)
    with c1:
        st.dataframe(vol_df.head(10), hide_index=True)
        
    with c2:
        top_vol = vol_df.head(10)

        fig_vol = px.bar(
            top_vol, 
            x='Ticker', 
            y='Volatility',
            title="Top 10 Most Volatile Stocks",
            color='Volatility',           
            text_auto='.4f'                 # OPTIONAL: Writes the exact value on top of the bar
        )

            # This renders the interactive chart with Tooltips
        st.plotly_chart(fig_vol, use_container_width=True)
        
    st.subheader("Cumulative Growth (Top 5)")
    top5 = yearly_ret.head(5)['Ticker'].tolist()
    new_df = get_cumulative_returns(df, top5)
    fig_cum = px.line(
        new_df, 
        x='date', 
        y='Cumulative_Return', 
        color='Ticker',               # This automatically creates separate lines & legend
        title="Growth of $1 Investment",
        markers=False
    )

        # Optional: Improve layout (add grid, rename axes)
    fig_cum.update_layout(
        xaxis_title="Date",
        yaxis_title="Cumulative Return",
        hovermode="x unified" ,        # Shows values for ALL lines when you hover over a date
        title_x=0.4,
        font=dict(color="black"),  # Makes all general text darker
        plot_bgcolor="white"
    )

    fig_cum.update_xaxes(
        showline=True, linewidth=2, linecolor='black', mirror=True,  # Thick black border
        showgrid=True, gridcolor='lightgrey',                        # Visible grid
        title_font=dict(size=14, color='black', family="Arial Black"), # Darker Title
        tickfont=dict(color='black')                                 # Darker Ticks
    )

        # Update Y-Axis (Left Border & Labels)
    fig_cum.update_yaxes(
        showline=True, linewidth=2, linecolor='black', mirror=True,  # Thick black border
        showgrid=True, gridcolor='lightgrey',
        title_font=dict(size=14, color='black', family="Arial Black"),
        tickfont=dict(color='black')
    )

        # Render in Streamlit
    st.plotly_chart(fig_cum, use_container_width=True)