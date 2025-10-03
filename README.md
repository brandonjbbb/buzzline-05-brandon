Brandon’s Custom Producer & Consumer
Producer: producer_brandon.py
Generates JSON messages and writes them into a local file messages.jsonl.
Simulates real-time by writing one message at a time.
Run:
python3 -m producers.producer_brandon
About My Custom Consumer
My custom consumer, file_consumer_brandon.py, ingests JSON messages from a local file (messages.jsonl) one at a time. For each message, it extracts the sentiment score, categorizes it as Positive, Neutral, or Negative, and stores the result in a persistent SQLite database (sentiment_results.db). This approach simulates real-time processing while keeping the setup lightweight (no Kafka cluster required). The stored data makes it easy to analyze sentiment trends across authors and categories, turning raw messages into actionable insights.
Consumer: file_consumer_brandon.py
Reads one message at a time from messages.jsonl.
Extracts the sentiment score and assigns a label:
0.2 → Positive
< -0.2 → Negative
Otherwise → Neutral
Stores results in a persistent SQLite database sentiment_results.db.
Run:
python3 -m consumers.file_consumer_brandon
Why this is interesting
This consumer transforms raw messages into actionable insights by classifying each message’s sentiment.
You can then analyze sentiment trends by author or category in real time.
Example: Query the Database
After running producer + consumer, view the results:
sqlite3 sentiment_results.db "SELECT * FROM sentiments LIMIT 10;"
Example output:
1|Charlie|2025-01-29 14:35:20|humor|0.87|Positive
2|Alice|2025-01-29 15:02:10|work|-0.45|Negative