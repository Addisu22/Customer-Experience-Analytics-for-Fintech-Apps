import cx_Oracle
import pandas as pd
from datetime import datetime

# Connect to Oracle XE
conn = cx_Oracle.connect("your_username", "your_password", "localhost/XEPDB1")
cursor = conn.cursor()

# Read cleaned data
df = pd.read_csv("data/bank_cleaned_reviews.csv")

# Insert banks
banks = df['bank_name'].unique()
bank_id_map = {}
for bank in banks:
    cursor.execute("INSERT INTO Banks (name) VALUES (:1) RETURNING bank_id INTO :2", [bank, cursor.var(cx_Oracle.NUMBER)])
    bank_id = cursor.fetchone()[0]
    bank_id_map[bank] = bank_id

# Insert reviews
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Reviews (bank_id, review_text, sentiment, rating, review_date)
        VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'))
    """, (
        bank_id_map[row['bank_name']],
        row['review_text'],
        row['sentiment'],
        row['rating'],
        row['review_date'][:10]  # Ensure format
    ))

conn.commit()
cursor.close()
conn.close()
