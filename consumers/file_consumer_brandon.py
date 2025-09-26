import json
import sqlite3
import time
import os

# Always store DB in project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_NAME = os.path.join(BASE_DIR, "sentiment_results.db")

INPUT_FILE = "messages.jsonl"  # each line = one JSON message

def create_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sentiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT,
            timestamp TEXT,
            category TEXT,
            sentiment_score REAL,
            sentiment_label TEXT
        )
    ''')
    conn.commit()
    conn.close()

def label_sentiment(score: float) -> str:
    if score > 0.2:
        return "Positive"
    elif score < -0.2:
        return "Negative"
    else:
        return "Neutral"

def process_message(message: dict):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    sentiment_score = message.get("sentiment", 0.0)
    sentiment_label = label_sentiment(sentiment_score)

    c.execute('''
        INSERT INTO sentiments (author, timestamp, category, sentiment_score, sentiment_label)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        message.get("author"),
        message.get("timestamp"),
        message.get("category"),
        sentiment_score,
        sentiment_label
    ))

    conn.commit()
    conn.close()
    print(f"Stored: {message.get('author')} | {sentiment_score} → {sentiment_label}")

def main():
    create_table()
    file_path = os.path.join(BASE_DIR, INPUT_FILE)

    if not os.path.exists(file_path):
        print(f"Input file {file_path} not found. Exiting.")
        return

    with open(file_path, "r") as f:
        for line in f:
            try:
                message = json.loads(line.strip())
                process_message(message)
                time.sleep(1)  # simulate streaming, 1 second delay
            except json.JSONDecodeError:
                continue

if __name__ == "__main__":
    main()
