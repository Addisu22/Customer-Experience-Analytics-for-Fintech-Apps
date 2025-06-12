 Task-Specific Breakdown
📦 Task 1: Data Collection and Preprocessing
scraper.py

Use google-play-scraper or google_play_scraper from PyPI.

preprocess.py

Normalize dates to YYYY-MM-DD

Drop missing & duplicate entries

Save as: cleaned_reviews.csv

✅ Commit to task-1 branch
✅ Add .gitignore, __init__.py, requirements.txt
✅ Update README with scraping method

📊 Task 2: Sentiment & Thematic Analysis
sentiment_analysis.py

Use transformers for DistilBERT or fallback to VADER

Add review_id, sentiment_score, sentiment_label

theme_analysis.py

Use spaCy or TF-IDF for keywords

Cluster to 3–5 themes per bank

Save: sentiment_themes.csv

✅ Commit to task-2 branch
✅ Use modular functions and comments
✅ Document theme grouping logic

🗃️ Task 3: Oracle DB Integration
create_tables.sql

sql
Copy
Edit
CREATE TABLE Banks (
    bank_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR2(100) UNIQUE
);

CREATE TABLE Reviews (
    review_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    bank_id NUMBER,
    review_text CLOB,
    sentiment VARCHAR2(20),
    rating NUMBER,
    review_date DATE,
    FOREIGN KEY (bank_id) REFERENCES Banks(bank_id)
);
insert_reviews.py

Connect using cx_Oracle

Insert CSV data to Oracle tables

✅ Create oracle_cleaned_reviews.csv
✅ Commit SQL dump oracle_dump.sql
✅ Push code and SQL files to task-3 branch

📈 Task 4: Insights & Recommendations
insights.py

Compare ratings/sentiments by bank

Identify top 2 satisfaction drivers and pain points

visualizations.py

Bar plot: average sentiment per bank

Word cloud: themes

Heatmap or histogram: rating distribution

✅ Commit visuals + PDF report to task-4 branch
✅ At least 2 plots, 1 driver, 1 pain point per bank
✅ Discuss bias and ethical issues