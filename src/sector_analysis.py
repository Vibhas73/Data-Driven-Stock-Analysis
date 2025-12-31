import streamlit as st
import plotly.express as px

def get_sector_performance(yearly_ret):
    """NEW: Calculates Average Yearly Return by Sector"""
    # Get yearly returns per stock first
    stock_returns = yearly_ret
        
    # Group by Sector and calculate mean return
    sector_perf = stock_returns.groupby('Sector')['Yearly_Return'].mean().reset_index()
    return sector_perf.sort_values(by='Yearly_Return', ascending=False)

def sector_analysis_tab(yearly_ret):
    st.subheader("Sector-wise Performance Analysis")
    st.write("Average Yearly Return per Sector. This helps identify which industries are booming (e.g., IT vs Banking).")
        
    sector_df = get_sector_performance(yearly_ret)
        
        # Display Bar Chart
    fig_sec = px.bar(sector_df, x='Sector', y='Yearly_Return', 
                    color='Yearly_Return', 
                    title="Average Yearly Return by Sector",
                    text_auto='.2%',
                    color_continuous_scale='Viridis')
    
    fig_sec.update_layout(
        title_x=0.4,
        font=dict(color="black"),  # Makes all general text darker
        plot_bgcolor="white"
    )
        
    st.plotly_chart(fig_sec, use_container_width=True)
        
    with st.expander("View Sector Data Details"):
        st.dataframe(sector_df, hide_index=True)