import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute(
        "UPDATE movies SET duration = 100 "
        "WHERE genre_id = (SELECT id FROM genres WHERE name = 'мюзикл') AND duration > 100"
    )
    conn.commit()
    conn.close()


if __name__ == '__main__':
    name = input()
    get_result(name)
