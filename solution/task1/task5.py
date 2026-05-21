import sqlite3

db_name = input()
artist_name = input()
conn = sqlite3.connect(db_name)
cur = conn.cursor()
cur.execute("""
    SELECT DISTINCT t.Name
    FROM Track t
    JOIN Album al ON t.AlbumId = al.AlbumId
    JOIN Artist ar ON al.ArtistId = ar.ArtistId
    WHERE ar.Name = ?
    ORDER BY t.Name
""", (artist_name,))
for (name,) in cur.fetchall():
    print(name)
conn.close()
