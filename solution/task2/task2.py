import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("UPDATE movies SET duration = 42 WHERE duration IS NULL")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    name = input()
    get_result(name)
