import cx_Oracle
import pandas as pd
from datetime import datetime
user = "bank_reviews"
password ="System123#"
dsn = "localhost/XEPDB1"

def connect_to_oracle(user, password, dsn):
    try:
        connection = cx_Oracle.connect(username, password, dsn)
        print("Connected to Oracle DB")
        return connection
    except cx_Oracle.DatabaseError as e:
        print("Connection failed:", e)
        return None

def insert_data(connection, df):
    cursor = connection.cursor()
    bank_id_map = {}

    # Insert unique banks
    for bank in df['bank_name'].unique():
        cursor.execute("SELECT bank_id FROM Banks WHERE name = :1", [bank])
        result = cursor.fetchone()
        if result:
            bank_id = result[0]
        else:
            cursor.execute("INSERT INTO Banks (name) VALUES (:1) RETURNING bank_id INTO :2", [bank, cursor.var(cx_Oracle.NUMBER)])
            bank_id = cursor.getimplicitresults()[0][0]
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
            int(row['rating']),
            row['review_date']
        ))

    connection.commit()
    print(f"✅ Inserted {len(df)} reviews")
    cursor.close()

