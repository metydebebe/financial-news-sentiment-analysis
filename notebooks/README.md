# Predicting Price Moves with News Sentiment

## Exploratory Data Analysis (EDA) of Financial News Headlines

### Overview

The `EDA_Financial_News.ipynb` notebook performs an exploratory data analysis on a dataset of financial news headlines. This analysis aims to uncover insights related to publication trends, descriptive statistics, and keyword identification within the headlines.

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

### Conclusion

The notebook effectively demonstrates various exploratory data analysis techniques and provides visualizations that help interpret the dataset. Users can gain insights into the financial news landscape through the analysis presented in this notebook.

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
