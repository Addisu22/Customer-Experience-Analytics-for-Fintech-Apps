import pandas as pd

def preprocess_reviews(file_path, output_path):
    df = pd.read_csv(file_path)

    # Drop duplicates
    df.drop_duplicates(subset=['Review Description'], inplace=True)

    # Drop rows with missing critical values
    df.dropna(subset=['Review Description', 'Rating', 'Date', 'Bank'], inplace=True)

    # Normalize date
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.date
    df.dropna(subset=['Date'], inplace=True)

    # Add source
    df['source'] = 'Google Play Store'

    # Save cleaned CSV
    df[['Review Description', 'Rating', 'Date', 'Bank', 'Source']].to_csv(output_path, index=False)

    print(f"Preprocessed data saved to {output_path}")
    return df