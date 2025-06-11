# Bank App Review Scraper 

This project scrapes and preprocesses reviews from the Google Play Store for three major Ethiopian bank apps: CBE, BOA, and Dashen.

## 🛠️ Features

- Scrapes 400+ reviews per Bank App
- Extracts review content, ratings, and dates
- Preprocesses data (removes duplicates, normalizes dates)
- Saves as a clean CSV for downstream NLP analysis

## Target Bank Apps

| Bank    | App ID                           |
|---------|----------------------------------|
| CBE     | com.combanketh.mobilebanking     |
| BOA     | com.bankofabyssinia.boaapp       |
| Dashen  | com.dashen.dashensuperapp        |

##  How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run main script
python src/main.py
