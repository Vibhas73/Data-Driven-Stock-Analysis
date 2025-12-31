import streamlit as st
import pandas as pd
import plotly.express as px

def performance_tab(yearly_ret):
    st.subheader("Top 10 Gainers vs Losers")
    top_gainers = yearly_ret.head(10)
    top_losers  = yearly_ret.tail(10)
    c1, c2 = st.columns(2, border=True)
    with c1:
        st.subheader("Top 10 Gainers")
        fig_gain = px.bar(
            top_gainers, 
            x='Ticker', 
            y='Yearly_Return', 
            color='Yearly_Return',              # Optional: Gradient Green
            color_continuous_scale='Greens',    # Theme
            title="Top 10 Gainers",
            text_auto='.2%'                     # Shows percentage on bars
        )
            
        fig_gain.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig_gain, use_container_width=True)

    with c2:
        st.subheader("Top 10 Losers")
        fig_loss = px.bar(
            top_losers, 
            x='Ticker', 
            y='Yearly_Return', 
            color='Yearly_Return',              # Optional: Gradient Red
            color_continuous_scale='Reds_r',    # Theme (Reversed so darker red = bigger loss)
            title="Top 10 Losers",
            text_auto='.2%'
        )
            
        fig_loss.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig_loss, use_container_width=True)