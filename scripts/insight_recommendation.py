import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from textblob import TextBlob
import warnings

warnings.filterwarnings('ignore')
plt.style.use('ggplot')

# Sample Data Generation (Replace with real data)
def generate_sample_data():
    """Generates synthetic app review data for CBE, BOA, and Dashenh Bank.

    Returns:
        pd.DataFrame: Sample dataset with columns ['bank', 'rating', 'review', 'date'].
    """
    np.random.seed(42)
    banks = ['CBE', 'BOA', 'Dashen']
    reviews = [
        "Great app, very fast!",
        "Crashes frequently, needs improvement.",
        "Customer support is slow.",
        "Easy to use, love it!",
        "Transactions fail sometimes.",
        "UI is outdated.",
        "Best banking app in Ethiopia!",
        "Takes too long to load.",
        "Very reliable for mobile banking.",
        "Needs more features."
    ]

    data = {
        'bank': np.random.choice(banks, 100),
        'rating': np.random.randint(1, 6, 100),
        'review': np.random.choice(reviews, 100),
        'date': pd.date_range('2023-01-01', periods=100, freq='D')
    }
    return pd.DataFrame(data)

# Sentiment Analysis
def analyze_sentiment(text):
    """Performs sentiment analysis using TextBlob.

    Args:
        text (str): Review text.

    Returns:
        str: 'Positive', 'Neutral', or 'Negative'.
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.1:
        return 'Positive'
    elif analysis.sentiment.polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

# Visualization Functions
def plot_sentiment_trend(df):
    """Plots sentiment trend over time for each bank.

    Args:
        df (pd.DataFrame): Data containing 'bank', 'date', and sentiment.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=df,
        x='date',
        y='sentiment_score',
        hue='bank',
        ci=None
    )
    plt.title('Sentiment Trend Over Time (CBE vs. BOA vs. Dashen)')
    plt.ylabel('Sentiment Score')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plots/sentiment_trend.png')
    plt.show()

def plot_rating_distribution(df):
    """Plots rating distribution comparison between banks.

    Args:
        df (pd.DataFrame): Data containing 'bank' and 'rating'.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(
        data=df,
        x='bank',
        hue='rating',
        palette='viridis'
    )
    plt.title('Rating Distribution (1-5 Stars)')
    plt.xlabel('Bank')
    plt.ylabel('Number of Reviews')
    plt.legend(title='Rating')
    plt.tight_layout()
    plt.savefig('plots/rating_distribution.png')
    plt.show()