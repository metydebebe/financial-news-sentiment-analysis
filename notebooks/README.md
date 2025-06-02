# Predicting Price Moves with News Sentiment

## Exploratory Data Analysis (EDA) of Financial News Headlines and Correlation with Stock Movements

### Overview

This project analyzes the relationship between financial news sentiment and stock price movements. It includes exploratory data analysis on financial news headlines, technical analysis of stock prices, sentiment quantification, and correlation analysis between news sentiment and stock returns.

The analysis is split across notebooks:

EDA_Financial_News.ipynb: Performs exploratory data analysis on financial news headlines, including publication trends, descriptive statistics, keyword extraction, and publisher contributions.

Quantitative_Analysis.ipynb: Loads historical stock price data, computes technical indicators (SMA, RSI, MACD) using TA-Lib, fetches company financials via yfinance, and visualizes price trends.

Correlation_Analysis.ipynb (or integrated in notebooks): Aligns dates between news and stock data, performs sentiment analysis on news headlines, calculates daily stock returns, and computes the correlation between average daily sentiment and stock returns.

Key Steps in the Analysis
Dataset Loading
Load financial news headlines and historical stock price data with error handling for missing or malformed files.

Data Cleaning and Date Normalization
Convert and clean date columns in both news and stock datasets. Normalize timestamps by converting datetime columns to date-only format and removing timezone information to ensure proper alignment.

Sentiment Analysis
Apply sentiment analysis tools (e.g., nltk, TextBlob) to financial news headlines to assign sentiment scores (positive, negative, neutral).

Aggregation of Sentiment Scores
Aggregate multiple article sentiment scores per day by computing the average daily sentiment.

Stock Price Analysis
Calculate daily stock returns as percentage changes in closing prices to represent stock price movements.

Merging Datasets
Merge the daily aggregated sentiment scores with stock daily returns on the normalized date column.

Correlation Analysis
Compute the Pearson correlation coefficient between daily average sentiment scores and daily stock returns to quantify the relationship.

Visualization
Visualize sentiment versus daily returns using scatter plots with optional regression lines, and time series plots to observe trends over time.

Additional Analysis and Tools
Calculation of technical indicators such as 20-day and 50-day Simple Moving Averages (SMA), 14-day Relative Strength Index (RSI), and MACD using TA-Lib.

Fetching and incorporating company financial metrics via yfinance.

Handling missing data and resampling stock data to daily frequency with forward filling.

Visualization enhancements including transparency in scatter plots and dual-axis time series charts.

Requirements
Python 3.11

pandas

numpy

matplotlib

seaborn

yfinance

TA-Lib

nltk or TextBlob (for sentiment analysis)

Install dependencies with:

pip install pandas numpy matplotlib seaborn yfinance TA-Lib nltk textblob
Usage
Data Placement
Place your historical stock data CSV files (e.g., AAPL_historical_data.csv) in the ../data/yfinance_data/ directory.

Clone the Repository

git clone https://github.com/metydebebe/financial-news-sentiment-analysis
cd financial-news-sentiment-analysis
Set Up Your Environment

Install dependencies listed in requirements.txt:

pip install -r requirements.txt
Run the Notebooks

Open EDA_Financial_News.ipynb to explore news data.

Open Quantitative_Analysis.ipynb to analyze stock data and technical indicators.

Run correlation analysis cells or Correlation_Analysis.ipynb to align dates, perform sentiment aggregation, merge datasets, calculate daily returns, and compute correlation.
