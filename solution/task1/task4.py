import sqlite3

db_name = input()
conn = sqlite3.connect(db_name)
cur = conn.cursor()
cur.execute("""
    SELECT m.title
    FROM movies m
    JOIN genres g ON m.genre_id = g.id
    WHERE g.name = 'комедия' AND m.duration >= 60
""")
for (title,) in cur.fetchall():
    print(title)
conn.close()
