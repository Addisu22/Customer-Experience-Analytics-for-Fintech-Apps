"""
sentiment_vader_analysis.py

Performs sentiment scoring using VADER.
"""

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')


def compute_vader_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute sentiment scores using VADER.

    Parameters:
        df (pd.DataFrame): DataFrame with a 'review' column.

    Returns:
        pd.DataFrame: Original data with sentiment scores and labels.
    """
    sia = SentimentIntensityAnalyzer()

    def get_sentiment(row):
        scores = sia.polarity_scores(row)
        compound = scores['compound']
        if compound >= 0.05:
            return 'positive', compound
        elif compound <= -0.05:
            return 'negative', compound
        else:
            return 'neutral', compound

    df[['sentiment_label', 'sentiment_score']] = df['Review Description'].apply(
        lambda x: pd.Series(get_sentiment(str(x)))
    )
    return df
