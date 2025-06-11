"""
thematic_tfidf_spacy_analysis.py

Extracts keywords and assigns themes using TF-IDF and simple rules.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_keywords(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Extract top keywords from reviews using TF-IDF.

    Parameters:
        df (pd.DataFrame): DataFrame with 'review' column.
        top_n (int): Number of top keywords per bank.

    Returns:
        pd.DataFrame: Keywords and TF-IDF scores per bank.
    """
    result = []

    for bank in df['bank'].unique():
        subset = df[df['bank'] == bank]
        tfidf = TfidfVectorizer(ngram_range=(1, 2), stop_words='english', max_features=100)
        X = tfidf.fit_transform(subset['review'].astype(str))
        scores = zip(tfidf.get_feature_names_out(), X.sum(axis=0).A1)
        top_keywords = sorted(scores, key=lambda x: x[1], reverse=True)[:top_n]

        for keyword, score in top_keywords:
            result.append({'bank': bank, 'keyword': keyword, 'score': score})

    return pd.DataFrame(result)


def assign_themes(keyword: str) -> str:
    """
    Map keywords to high-level themes using rule-based logic.

    Parameters:
        keyword (str): A TF-IDF keyword.

    Returns:
        str: Theme name.
    """
    keyword = keyword.lower()
    if any(word in keyword for word in ['login', 'access', 'otp']):
        return "Account Access Issues"
    elif any(word in keyword for word in ['slow', 'fail', 'crash', 'hang']):
        return "Performance & Reliability"
    elif any(word in keyword for word in ['transfer', 'payment', 'transaction']):
        return "Transaction Problems"
    elif any(word in keyword for word in ['support', 'help', 'response']):
        return "Customer Support"
    elif any(word in keyword for word in ['ui', 'design', 'interface', 'easy', 'user', 'freindly']):
        return "User Interface & Experience"
    else:
        return "Other"


def tag_themes(df_keywords: pd.DataFrame) -> pd.DataFrame:
    """
    Assign themes to each keyword row.

    Parameters:
        df_keywords (pd.DataFrame): DataFrame with extracted keywords.

    Returns:
        pd.DataFrame: Keywords with assigned themes.
    """
    df_keywords['theme'] = df_keywords['keyword'].apply(assign_themes)
    return df_keywords