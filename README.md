# 📈 Nifty 50 Stock Analytics Dashboard
### Organizing, Cleaning, and Visualizing Market Trends
A comprehensive, interactive web application built with Python and Streamlit to analyze the historical performance, volatility, and correlation of Nifty 50 stocks. This dashboard provides actionable insights for traders and investors through dynamic visualizations.

## 🚀 Features
Based on the current build, the dashboard includes the following analytical modules:

### 1. 📊 Market Overview
KPI Metrics: Real-time summary of Total Stocks, Green vs. Red status, Average Price, and Average Volume.

Top Movers: Instantly identifies the Best Performer (e.g., TRENT) and Worst Performer (e.g., INDUSINDBK).

Sentiment Analysis: A pie chart visualizing the ratio of gaining stocks vs. losing stocks.

### 2. 🏆 Performance Analysis
Gainers & Losers: Ranked bar charts displaying the top 10 stocks by yearly return.

Cumulative Growth: A "Growth of $1 Investment" time-series chart to visualize how capital would have compounded over time for specific tickers.

### 3. 📉 Volatility & Risk
Risk Ranking: Calculates the standard deviation (volatility) of daily returns to rank stocks from most stable to most volatile.

Visual Comparison: Bar charts identifying high-risk/high-reward stocks (e.g., TRENT, BEL).

### 4. 🔗 Correlation Matrix
Heatmap Visualization: A color-coded heatmap to analyze how stocks move in relation to one another.

Diversification Tool: Helps identify positive correlations (e.g., Adani Ent & Adani Ports) and negative correlations (hedging opportunities).

### 5. 🏭 Sector Analysis
Industry Breakdown: Aggregates performance by sector (e.g., Retail, Defense, Auto) to identify booming industries versus lagging ones.

Detailed Metrics: Drill-down views into average yearly returns per sector.

### 6. 📅 Monthly Deep Dive
Granular Analysis: Filter performance by specific months (e.g., Oct 2023) to see seasonal trends and monthly top/bottom performers.

## 🛠️ Tech Stack

**Frontend**: Streamlit (for web interface)

**Data Manipulation**: Pandas, pyyaml (for data cleaning and calculating returns/volatility)

**Visualization**: Plotly Express, matplotlib (for interactive charts)

**Database**: SQL / SQLAlchemy (for storing historical stock data)

## 🚀 Getting Started

### Prerequisites
* Python 3.12+
* Pip (Python package manager)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vibhas73/Data-Driven-Stock-Analysis
   git checkout develop
   cd Data-Driven-Stock-Analysis/

2. **Update Project dbSetup.py**
   Update your local SQL Servers user and password
   
2. **Run the Project with following commands:**
    ```bash
    pip install -r requirement.txt
    python -m venv env
    cd env/Scripts
    .\Activate.ps1
    cd ..
    cd .. 
    python data_processor.py
    python dbSetup.py
    streamlit run streamlit_app.py
