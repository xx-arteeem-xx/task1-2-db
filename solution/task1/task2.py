import sqlite3

db_name = input()
conn = sqlite3.connect(db_name)
cur = conn.cursor()
cur.execute("SELECT title FROM movies WHERE title LIKE '%?'")
for (title,) in cur.fetchall():
    print(title)
conn.close()
