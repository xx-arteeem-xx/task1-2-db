import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.db')


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def register():
    init_db()
    while True:
        try:
            username = input('Введите имя пользователя: ')
        except EOFError:
            break

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('SELECT id FROM users WHERE username = ?', (username,))
        if cur.fetchone():
            print('Пользователь с таким именем уже существует')
            conn.close()
            continue

        try:
            email = input('Введите email: ')
        except EOFError:
            conn.close()
            break

        cur.execute('SELECT id FROM users WHERE email = ?', (email,))
        if cur.fetchone():
            print('Пользователь с таким email уже существует')
            conn.close()
            continue

        try:
            password = input('Введите пароль: ')
            confirm = input('Подтвердите пароль: ')
        except EOFError:
            conn.close()
            break

        if password != confirm:
            print('Пароли не совпадают')
            conn.close()
            continue

        cur.execute(
            'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
            (username, email, password)
        )
        conn.commit()
        conn.close()
        print('Регистрация успешна')


if __name__ == '__main__':
    register()
