from google_play_scraper import Sort, reviews
import pandas as pd

def scrape_reviews_eng(app_id, bank_name, lang='eng', count=500):
    # scraping review from Play_Store
    all_reviews = []
    try:
        result, _ = reviews(
            app_id,
            country='et',  # Ethiopia
            lang=lang,        # defaults to 'en'
            count=count,
            sort=Sort.NEWEST  # defaults to Sort.NEWEST
        )
        # Creating DataFrame from reviews data
        for entry in result:
            all_reviews.append({
                'Review Description': entry.get('content', ''),
                'User': entry.get('userName', 'Anonymous'),
                'Rating': entry.get('score', None),
                'Date': entry.get('at', None),
                'Bank': bank_name,
                'Source': 'Google Play Store'
            })
        print(f"Scraped {len(all_reviews)} reviews for {bank_name}")
    except Exception as e:
        print(f"Failed to scrape {bank_name}: {e}")
    return all_reviews