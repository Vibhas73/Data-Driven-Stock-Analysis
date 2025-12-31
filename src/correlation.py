import streamlit as st
import pandas as pd
import plotly.express as px

def get_correlation_matrix(df):
    pivot_df = df.pivot_table(index='date', columns='Ticker', values='close')
    return pivot_df.corr()

def correlation_tab(df):
    st.subheader("Market Correlation Heatmap")
        # 1. Add a Filter Toggle
    view_option = st.radio("View Correlation For:", ["Selected Stocks Only", "All Stocks (Nifty 50)"], horizontal=True)
    corr_matrix = get_correlation_matrix(df).columns.tolist()
    # Get the full matrix first
    full_matrix = get_correlation_matrix(df)
    if view_option == "Selected Stocks Only":
        # Filter the matrix to show only what is selected in the Sidebar
        selected_tickers = st.multiselect("Select Specific Stocks", corr_matrix, default=corr_matrix[:5])
        if len(selected_tickers) < 2:
            st.warning("Please select at least 2 stocks in the sidebar to view correlation.")
        else:
            # Slice the matrix
            filtered_matrix = full_matrix.loc[selected_tickers, selected_tickers]
                
            st.write("Dark Red = Strong Positive Correlation. Blue = Negative Correlation.")
            fig_corr = px.imshow(
                filtered_matrix, 
                text_auto=".2f", # Shows numbers because we have space
                aspect="auto", 
                color_continuous_scale='RdBu_r',
                title="Correlation: Selected Stocks"
            )
            st.plotly_chart(fig_corr, use_container_width=True)
                
    else:
        # Show ALL stocks, but make it TALL enough to read
            
        # Dynamic Height: 25 pixels per stock ensures it's readable
        dynamic_height = max(600, len(full_matrix) * 25)
        st.write("Dark Red = Strong Positive Correlation. Blue = Negative Correlation.")
        fig_corr = px.imshow(
            full_matrix, 
            text_auto=False, # Disable numbers to reduce clutter
            aspect="auto", 
            height=dynamic_height, # <--- KEY FIX: Make it tall
            color_continuous_scale='RdBu_r',
            title="Correlation: Entire Market"
        )
            
        # Rotate labels so they don't overlap
        fig_corr.update_xaxes(tickangle=-90, side="bottom")
            
        st.plotly_chart(fig_corr, use_container_width=True)