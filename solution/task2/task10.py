import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.db')


def login():
    while True:
        try:
            username = input('Введите имя пользователя: ')
        except EOFError:
            break

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('SELECT password FROM users WHERE username = ?', (username,))
        row = cur.fetchone()
        conn.close()

        if not row:
            print('Пользователь не найден')
            continue

        try:
            password = input('Введите пароль: ')
        except EOFError:
            break

        if password != row[0]:
            print('Неверный пароль')
        else:
            print('Вход выполнен')


if __name__ == '__main__':
    login()
