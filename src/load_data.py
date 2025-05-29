import pandas as pd
import os

def load_csv(file_name):
    """Load a CSV file and return a DataFrame."""
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_name} is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Define the paths to the data directories
data_dir = os.path.join("..", "data")  # Adjusted path to go one directory up
yfinance_data_dir = os.path.join(data_dir, "yfinance_data")

# Load datasets
analyst_ratings = load_csv(os.path.join(data_dir, "raw_analyst_ratings.csv"))
aapl_data = load_csv(os.path.join(yfinance_data_dir, "AAPL_historical_data.csv"))
amzn_data = load_csv(os.path.join(yfinance_data_dir, "AMZN_historical_data.csv"))
goog_data = load_csv(os.path.join(yfinance_data_dir, "GOOG_historical_data.csv"))
meta_data = load_csv(os.path.join(yfinance_data_dir, "META_historical_data.csv"))
msft_data = load_csv(os.path.join(yfinance_data_dir, "MSFT_historical_data.csv"))
nvda_data = load_csv(os.path.join(yfinance_data_dir, "NVDA_historical_data.csv"))
tsla_data = load_csv(os.path.join(yfinance_data_dir, "TSLA_historical_data.csv"))

# Display the first few rows of one dataset to verify loading
if aapl_data is not None:
    print(aapl_data.head())