import json
import time

OUTPUT_FILE = "messages.jsonl"

messages = [
    {
        "message": "I just shared a meme! It was amazing.",
        "author": "Charlie",
        "timestamp": "2025-01-29 14:35:20",
        "category": "humor",
        "sentiment": 0.87,
        "keyword_mentioned": "meme",
        "message_length": 42
    },
    {
        "message": "Work is stressful today.",
        "author": "Alice",
        "timestamp": "2025-01-29 15:02:10",
        "category": "work",
        "sentiment": -0.45,
        "keyword_mentioned": "stress",
        "message_length": 28
    }
]

def main():
    with open(OUTPUT_FILE, "w") as f:
        for msg in messages:
            f.write(json.dumps(msg) + "\n")
            print(f"Produced: {msg['message']}")
            time.sleep(1)  # simulate real-time

if __name__ == "__main__":
    main()
