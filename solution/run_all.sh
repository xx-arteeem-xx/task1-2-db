#!/bin/bash
# Запуск всех задач с тестовыми данными

FILMS=/app/films.db
MUSIC=/app/music.db

echo "============================================"
echo "  Задачи №1 — SELECT-запросы"
echo "============================================"

echo ""
echo "--- Задача 1.1: фильмы жанров 'музыка' и 'анимация' с 1997 года ---"
echo "$FILMS" | python3 /app/solution/task1/task1.py
echo "(0 результатов — в тестовой БД эти жанры не представлены)"

echo ""
echo "--- Задача 1.2: фильмы, название которых заканчивается на '?' ---"
echo "$FILMS" | python3 /app/solution/task1/task2.py

echo ""
echo "--- Задача 1.3: годы фильмов, название которых начинается на 'Х' (без дублей) ---"
echo "$FILMS" | python3 /app/solution/task1/task3.py

echo ""
echo "--- Задача 1.4: комедии продолжительностью не менее 60 минут ---"
echo "$FILMS" | python3 /app/solution/task1/task4.py | head -10
echo "... (выведены первые 10)"

echo ""
echo "--- Задача 1.5: треки исполнителя 'Led Zeppelin' (алфавитный порядок) ---"
printf "%s\nLed Zeppelin\n" "$MUSIC" | python3 /app/solution/task1/task5.py | head -10
echo "... (выведены первые 10)"

echo ""
echo "============================================"
echo "  Задачи №2 — Модификация данных"
echo "============================================"

run_task2() {
    local num=$1
    local desc=$2
    local check_before=$3
    local check_after=$4

    echo ""
    echo "--- Задача 2.${num}: ${desc} ---"
    cp "$FILMS" "/app/films_t2_${num}.db"

    if [ -n "$check_before" ]; then
        before=$(python3 -c "
import sqlite3
conn = sqlite3.connect('/app/films_t2_${num}.db')
cur = conn.cursor()
cur.execute(\"$check_before\")
print(cur.fetchone()[0])
conn.close()
")
        echo "До: $before строк"
    fi

    echo "/app/films_t2_${num}.db" | python3 "/app/solution/task2/task${num}.py"

    if [ -n "$check_after" ]; then
        after=$(python3 -c "
import sqlite3
conn = sqlite3.connect('/app/films_t2_${num}.db')
cur = conn.cursor()
cur.execute(\"$check_after\")
print(cur.fetchone()[0])
conn.close()
")
        echo "После: $after строк/записей"
    fi
}

run_task2 1 "Удаление комедий" \
    "SELECT COUNT(*) FROM movies WHERE genre_id=(SELECT id FROM genres WHERE name='комедия')" \
    "SELECT COUNT(*) FROM movies WHERE genre_id=(SELECT id FROM genres WHERE name='комедия')"

run_task2 2 "Установка длительности 42 мин для фильмов без длительности" \
    "SELECT COUNT(*) FROM movies WHERE duration IS NULL" \
    "SELECT COUNT(*) FROM movies WHERE duration IS NULL"

run_task2 3 "Удвоение длительности фантастики" \
    "SELECT AVG(duration) FROM movies JOIN genres ON movies.genre_id=genres.id WHERE genres.name='фантастика' AND duration IS NOT NULL" \
    "SELECT AVG(duration) FROM movies JOIN genres ON movies.genre_id=genres.id WHERE genres.name='фантастика' AND duration IS NOT NULL"

run_task2 4 "Удаление фильмов на 'Я' и 'а'" \
    "SELECT COUNT(*) FROM movies WHERE title LIKE 'Я%а'" \
    "SELECT COUNT(*) FROM movies WHERE title LIKE 'Я%а'"

run_task2 5 "Удаление боевиков длительностью >= 90 мин" \
    "SELECT COUNT(*) FROM movies JOIN genres ON movies.genre_id=genres.id WHERE genres.name='боевик' AND duration>=90" \
    "SELECT COUNT(*) FROM movies JOIN genres ON movies.genre_id=genres.id WHERE genres.name='боевик' AND duration>=90"

run_task2 6 "Обрезка мюзиклов до 100 мин" \
    "SELECT COUNT(*) FROM movies JOIN genres ON movies.genre_id=genres.id WHERE genres.name='мюзикл' AND duration>100" \
    "SELECT COUNT(*) FROM movies JOIN genres ON movies.genre_id=genres.id WHERE genres.name='мюзикл' AND duration>100"

run_task2 7 "Уменьшение длительности фильмов 1973 года втрое" \
    "SELECT AVG(duration) FROM movies WHERE year=1973 AND duration IS NOT NULL" \
    "SELECT AVG(duration) FROM movies WHERE year=1973 AND duration IS NOT NULL"

run_task2 8 "Удаление фантастики до 2000 г. с длительностью > 90 мин" \
    "SELECT COUNT(*) FROM movies JOIN genres ON movies.genre_id=genres.id WHERE genres.name='фантастика' AND year<2000 AND duration>90" \
    "SELECT COUNT(*) FROM movies JOIN genres ON movies.genre_id=genres.id WHERE genres.name='фантастика' AND year<2000 AND duration>90"

echo ""
echo "--- Задача 2.9: Система регистрации пользователей ---"
rm -f /app/solution/task2/users.db
printf "alice\nalice@example.com\nqwerty123\nqwerty123\nbob\nbob@example.com\nsecret\nsecret\nalice\nother@mail.com\npass\npass\n" \
    | python3 /app/solution/task2/task9.py

echo ""
echo "--- Задача 2.10: Система авторизации ---"
printf "alice\nqwerty123\nbob\nwrong_password\ncharlie\n" \
    | python3 /app/solution/task2/task10.py

echo ""
echo "============================================"
echo "  Задачи №3 — ORM с SQLAlchemy"
echo "============================================"

TASK3=/app/solution/task3

# Чистый старт: удаляем БД если осталась от прошлого запуска
rm -f "$TASK3/library.db"

echo ""
echo "--- Задача 3.1: Создание модели Author ---"
python3 "$TASK3/task1.py"

echo ""
echo "--- Задача 3.2: Добавление трёх авторов ---"
python3 "$TASK3/task2.py"

echo ""
echo "--- Задача 3.3: Вывод всех авторов ---"
python3 "$TASK3/task3.py"

echo ""
echo "--- Задача 3.4: Вывод авторов из России ---"
python3 "$TASK3/task4.py"

echo ""
echo "--- Задача 3.5: Создание модели Book ---"
python3 "$TASK3/task5.py"

echo ""
echo "--- Задача 3.6: Добавление трёх книг ---"
python3 "$TASK3/task6.py"

echo ""
echo "--- Задача 3.7: Вывод всех книг ---"
python3 "$TASK3/task7.py"

echo ""
echo "--- Задача 3.8: Вывод книг после 1860 г. стоимостью до 300 руб. ---"
python3 "$TASK3/task8.py"

echo ""
echo "============================================"
echo "  Все задачи выполнены успешно!"
echo "============================================"
