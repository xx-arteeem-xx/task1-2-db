import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("UPDATE movies SET duration = duration / 3 WHERE year = 1973")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    name = input()
    get_result(name)
