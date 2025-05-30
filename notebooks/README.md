# Predicting Price Moves with News Sentiment

## Exploratory Data Analysis (EDA) of Financial News Headlines

### Overview

The `EDA_Financial_News.ipynb` notebook performs an exploratory data analysis on a dataset of financial news headlines. This analysis aims to uncover insights related to publication trends, descriptive statistics, and keyword identification within the headlines.

The `Quantitative_Analysis.ipynb` notebook loads historical stock data (e.g., for Apple Inc.), computes technical indicators such as Simple Moving Averages (SMA), Relative Strength Index (RSI), and MACD using TA-Lib, retrieves financial metrics via yfinance, and visualizes price trends and moving averages.

### Key Steps in the Analysis

1. **Dataset Loading**:

   - The notebook begins by loading the analyst ratings dataset from a CSV file. It includes error handling to manage potential issues such as missing files or empty datasets.

2. **Descriptive Statistics**:

   - Basic statistics of the dataset are calculated, including summary statistics, headline lengths, article counts per publisher, and trends over time based on publication dates.

3. **Text Analysis (Topic Modeling)**:

   - Natural Language Processing (NLP) techniques are utilized to identify keywords in the headlines, providing insights into the most common terms used.

4. **Time Series Analysis**:

   - The frequency of article publications over time is analyzed and visualized, helping to identify trends and patterns in the data.

5. **Publisher Analysis**:

   - The contributions of various publishers to the dataset are examined, displaying the number of articles published by each publisher in a bar chart.

6. **Loads historical stock price data from CSV**

7. **Calculates**

20-day and 50-day Simple Moving Averages (SMA)

14-day Relative Strength Index (RSI)

MACD and MACD Signal line

8. **Fetches company financials using yfinance**

9. **Plots closing price alongside moving averages**

10. **Handles common data loading errors gracefully**

## Requirements

Python 3.7+

pandas

numpy

matplotlib

yfinance

TA-Lib

Install dependencies with:

pip install pandas numpy matplotlib yfinance TA-Lib

## Usage

Place your historical stock data CSV (e.g., AAPL_historical_data.csv) in the ../data/yfinance_data/ directory.

### Clone the Repository

git clone https://github.com/metydebebe/financial-news-sentiment-analysis
cd financial-news-sentiment-analysis

### Running the Notebook

To execute the analysis:

1. Ensure the dataset is available in the specified directory (data/).
2. Set Up Your Environment:
   Install the dependencies listed in `requirements.txt` by running:
   pip install -r requirements.txt
3. Open the Notebook: Launch Jupyter Notebook and open EDA_Financial_News.ipynb.
4. Run the cells
