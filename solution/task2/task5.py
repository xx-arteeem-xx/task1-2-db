import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM movies "
        "WHERE genre_id = (SELECT id FROM genres WHERE name = 'боевик') AND duration >= 90"
    )
    conn.commit()
    conn.close()


if __name__ == '__main__':
    name = input()
    get_result(name)
