import sqlite3

db_name = input()
conn = sqlite3.connect(db_name)
cur = conn.cursor()
cur.execute("""
    SELECT m.title
    FROM movies m
    JOIN genres g ON m.genre_id = g.id
    WHERE g.name IN ('музыка', 'анимация') AND m.year >= 1997
""")
for (title,) in cur.fetchall():
    print(title)
conn.close()
