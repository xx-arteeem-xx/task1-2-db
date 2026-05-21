import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("DELETE FROM movies WHERE title LIKE 'Я%а'")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    name = input()
    get_result(name)
