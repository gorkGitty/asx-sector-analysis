import yfinance as yf
import pandas as pd

# Define tickers and sectors
ticker = ["^AXJO", "ATEC.AX", "MVR.AX", "QFN.AX", "SLF.AX"]
start_date = "2021-01-01"
end_date = "2025-03-31"
sector_map = {
    "^AXJO": "Index",
    "ATEC.AX": "Technology",
    "MVR.AX": "Resources",
    "QFN.AX": "Financials",
    "SLF.AX": "Property"
}

# Download data
data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
adj_close = data["Adj Close"]
volume = data["Volume"]

# Calculate metrics
daily_returns = adj_close.pct_change()
volatility = daily_returns.std()
annualized_volatility = volatility * (252 ** 0.5)
cumulative_return = (adj_close.iloc[-1] / adj_close.iloc[0]) - 1
num_years = (adj_close.index[-1] - adj_close.index[0]).days / 365.25
annualized_return = (adj_close.iloc[-1] / adj_close.iloc[0]) ** (1/num_years) - 1
normalized_close = adj_close / adj_close.iloc[0] * 100

# Create metrics DataFrame
metrics_data = pd.DataFrame({
    'Ticker': ticker,
    'Sector': [sector_map[t] for t in ticker],
    'Cumulative_Return': cumulative_return,
    'Annualized_Return': annualized_return,
    'Daily_Volatility': volatility,
    'Annualized_Volatility': annualized_volatility
})

# Create daily data DataFrame
daily_data = pd.DataFrame()
daily_data['Date'] = adj_close.index.repeat(len(ticker))
daily_data['Ticker'] = ticker * len(adj_close.index)
daily_data['Normalized_Close'] = normalized_close.values.flatten()
daily_data['Daily_Return'] = daily_returns.values.flatten()
daily_data['Sector'] = daily_data['Ticker'].map(sector_map)

# Round metrics
metrics_data = metrics_data.round({
    'Cumulative_Return': 3,
    'Annualized_Return': 3,
    'Daily_Volatility': 4,
    'Annualized_Volatility': 3})

# Export to CSV
metrics_data.to_csv("ASX_Sector_Performance_Metrics.csv", index=False)
daily_data.to_csv("ASX_Sector_Performance_Daily.csv", index=False)

print("Data exported!")