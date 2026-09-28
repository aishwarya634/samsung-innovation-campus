# Import Pandas for data analysis
import pandas as pd

# Import NumPy for numerical operations
import numpy as np

# Import datetime for working with dates
import datetime

# Import Matplotlib for visualization
import matplotlib.pyplot as plt

# Import yfinance to download financial data from Yahoo Finance
import yfinance as yf

# Import specific date/time classes
from datetime import date, datetime, time, timezone
# Function to download stock price data
# ticker = stock symbol
# start  = starting date
# end    = ending date

def get_stock_data(ticker, start, end):

    # Download stock data from Yahoo Finance
    # auto_adjust=False keeps the original prices
    data = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=False
    )

    # Check whether the downloaded DataFrame has MultiIndex columns
    if isinstance(data.columns, pd.MultiIndex):

        # Convert MultiIndex columns into normal one-level columns
        data.columns = data.columns.get_level_values(0)

    # Remove duplicate column names, if any
    data = data.loc[:, ~data.columns.duplicated()]

    # Convert the Date index into a normal column
    data = data.reset_index()

    # Add a column containing the ticker symbol
    data["Ticker"] = ticker

    # Return the processed DataFrame
    return data
# Disney's ticker symbol
ticker = 'SPY'

# Starting date: January 1, 2025
start = datetime(2025, 1, 1)

# Ending date: today's date
end = datetime.today()
# Download Disney stock data
d = get_stock_data(ticker, start, end)

# Display the first five rows
print(d.head())
# Convert the data so:
# rows    -> Date
# columns -> Ticker
# values  -> Closing price

d = d.pivot(
    index="Date",
    columns="Ticker",
    values="Close"
)

# Display the first five rows
print(d.head())
# Download data for all seven financial instruments

SPY = get_stock_data("SPY", start, end)

IYW = get_stock_data("IYW", start, end)

VT = get_stock_data("VT", start, end)

DBA = get_stock_data("DBA", start, end)

TLT = get_stock_data("TLT", start, end)

PDBC = get_stock_data("PDBC", start, end)

IAU = get_stock_data("IAU", start, end)
print(SPY.info())
# Convert each DataFrame into:
# Date -> rows
# Ticker -> columns
# Close -> values

SPY = SPY.reset_index().pivot(
    index="Date",
    columns="Ticker",
    values="Close"
)

IYW = IYW.reset_index().pivot(
    index="Date",
    columns="Ticker",
    values="Close"
)

VT = VT.reset_index().pivot(
    index="Date",
    columns="Ticker",
    values="Close"
)

DBA = DBA.reset_index().pivot(
    index="Date",
    columns="Ticker",
    values="Close"
)

TLT = TLT.reset_index().pivot(
    index="Date",
    columns="Ticker",
    values="Close"
)

PDBC = PDBC.reset_index().pivot(
    index="Date",
    columns="Ticker",
    values="Close"
)

IAU = IAU.reset_index().pivot(
    index="Date",
    columns="Ticker",
    values="Close"
)
# Combine all seven DataFrames side-by-side
# axis=1 means concatenate by columns
# join='outer' keeps all dates available in the DataFrames

stock = pd.concat(
    [SPY, IYW, VT, DBA, TLT, PDBC, IAU],
    axis=1,
    join='outer'
)

# Display the first five rows
print(stock.head())
# Use ggplot-style visualization
plt.style.use('ggplot')

# Plot all stock closing prices
# figsize controls the size of the graph
stock.plot(figsize=(20, 10))

# Display the graph
plt.show()
# Select the period from January 1, 2025
# through November 30, 2025

macro_shock = stock['2025-1-1':'2025-11-30']
# Apply ggplot-style visualization
plt.style.use('ggplot')

# Plot the selected period
macro_shock.plot(figsize=(20, 10))

# Display the graph
plt.show()
# Get the dates
x = macro_shock.index

# SPY = general stock market
s_y = macro_shock[['SPY']]

# IAU = gold
i_y = macro_shock[['IAU']]

# TLT = bond ETF
t_y = macro_shock[['TLT']]
# Import Matplotlib
import matplotlib.pyplot as plt

# Create 3 graphs arranged vertically
fig, axs = plt.subplots(
    1,
    3,
    figsize=(15, 5)
)

# Plot SPY
axs[0].plot(x, s_y)

# Plot IAU
axs[1].plot(x, i_y)

# Plot TLT
axs[2].plot(x, t_y)

# Rotate the x-axis labels
# on all three graphs
for ax in axs:
    ax.tick_params(
        axis='x',
        rotation=45
    )

# Give the complete figure a title
fig.suptitle('Macro Shock')

# Display the graphs
plt.show()
# PDBC represents the raw-material/commodity-related data
ticker = 'PDBC'

# Starting date
start = datetime(2025, 1, 1)

# Ending date
end = datetime.today()
# Download PDBC data
df = get_stock_data(ticker, start, end)

# Display the first five rows
df.head()
# Remove all columns except:
# Date and Volume

df = df.drop(
    ['Ticker', 'High', 'Low', 'Open', 'Close', 'Adj Close'],
    axis=1
)

# Display the first five rows
df.head()
# x-axis = DataFrame index
x = df['Data']

# y-axis = trading volume
y = df['Volume']

# Create a large figure
plt.figure(figsize=(15, 3))

# Draw a bar graph
plt.bar(x, y)

# Display the graph
plt.show()
# Select PDBC
ticker = 'PDBC'

# Starting date
start = datetime(2025, 1, 1)

# Ending date
end = datetime.today()
# Download PDBC data
df = get_stock_data(ticker, start, end)
# Create a figure of size 12 x 8
fig = plt.figure(figsize=(12, 8))

# Create the upper grid
# 4 rows x 4 columns
# Start at row 0, column 0
# Use 3 rows and 4 columns
top_grid = plt.subplot2grid(
    (4, 4),
    (0, 0),
    rowspan=3,
    colspan=4
)

# Create the lower grid
# Start at row 3, column 0
# Use 1 row and 4 columns
bottom_grid = plt.subplot2grid(
    (4, 4),
    (3, 0),
    rowspan=1,
    colspan=4
)

# Plot closing price in the upper graph
top_grid.plot(
    df.index,
    df['Close'],
    label='Close'
)

# Plot trading volume in the lower graph
bottom_grid.plot(
    df.index,
    df['Volume'],
    label='Volume'
)

# Automatically adjust spacing
plt.tight_layout()

# Display legend
plt.legend()

# Display the complete figure
plt.show()
# Display the first five rows of stock data
print(stock.head())
# Select only the SPY closing-price series
print(stock['SPY'])
# Shift the SPY data by one row
# This gives the previous day's closing price

print(stock['SPY'].shift(1))
# Calculate daily percentage change

spy_daily_pc = (
    stock['SPY'] /
    stock['SPY'].shift(1) - 1
) * 100

# Display the result
print(spy_daily_pc)
# Replace the first missing percentage-change value with 0

spy_daily_pc.iloc[0] = 0
# Plot the daily percentage change
spy_daily_pc.plot()

# Display the graph
plt.show()
# Create a histogram with 50 bins
# bins=50 divides the percentage changes
# into 50 intervals

plt.hist(
    spy_daily_pc,
    bins=50
)

# Display the histogram
plt.show()
# Calculate daily percentage change
# for all seven tickers at once

stock_daily_pc = (
    (stock - stock.shift(1))
    / stock.shift(1)
) * 100

# Display the first five rows
stock_daily_pc.head()
# Calculate cumulative return
# by cumulatively adding the daily percentage changes

stock_d_cr = stock_daily_pc.cumsum()
# Display the cumulative return DataFrame
print(stock_d_cr)
# Plot cumulative returns for all tickers
stock_d_cr.plot(
    figsize=(20, 10)
)

# Display the graph
plt.show()
# Calculate correlation between
# daily percentage changes of all tickers

df_corr = stock_daily_pc.corr()

# Display the correlation matrix
print(df_corr)
# Display the correlation matrix as an image
# cmap='hot' controls the color mapping
# interpolation='none' keeps the cells sharp

plt.imshow(
    df_corr,
    cmap='hot',
    interpolation='none'
)

# Display the color scale
plt.colorbar()

# Add ticker names to x-axis
plt.xticks(
    range(len(df_corr)),
    df_corr.columns
)

# Add ticker names to y-axis
plt.yticks(
    range(len(df_corr)),
    df_corr.columns
)

# Set figure size
plt.gcf().set_size_inches(10, 10)

# Display the heatmap
plt.show()
# Compare SPY and VT correlation values
plt.scatter(
    df_corr.SPY,
    df_corr.VT
)

# Display the graph
plt.show()
# Number of days used for the rolling window
periods = 75

# Calculate rolling standard deviation
# using a 75-day window

vol = stock_daily_pc.rolling(
    window=periods
).std()

# Display volatility values
print(vol)
# Plot SPY volatility
vol["SPY"].plot()

# Plot TLT volatility
vol["TLT"].plot()

# Plot DBA volatility
vol["DBA"].plot()

# Display the graph
plt.show()