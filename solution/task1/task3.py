import sqlite3

db_name = input()
conn = sqlite3.connect(db_name)
cur = conn.cursor()
cur.execute("SELECT DISTINCT year FROM movies WHERE title LIKE 'Х%' ORDER BY year")
for (year,) in cur.fetchall():
    print(year)
conn.close()
