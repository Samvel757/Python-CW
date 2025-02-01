import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="second",
    user="postgres",
    password="15032009sg2009",
    host="localhost",
    port="5432"
)

# Создаём объект-курсор
cur = conn.cursor()

# 1. Создание таблицы, если её нет
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER,
        email VARCHAR(100) UNIQUE
    );
""")
conn.commit()
print("Таблица создана")

# 2. Вставка данных
cur.execute("""
    INSERT INTO users (name, age, email) 
    VALUES (%s, %s, %s);
""", ("Саша", 19, "sanya@example.com"))

conn.commit()
print("Данные добавлены")

# 3. Чтение данных
cur.execute("SELECT * FROM users;")
users = cur.fetchall()

print("Список пользователей:")
for user in users:
    print(user)

# 4. Обновление данных
cur.execute("""
    UPDATE users 
    SET age = %s 
    WHERE name = %s;
""", (18, "Саша"))

conn.commit()
print("Данные обновлены")

# 5. Удаление данных
cur.execute("""
    DELETE FROM users 
    WHERE name = %s;
""", ("Саша",))

conn.commit()
print("Данные удалены")

# Закрытие соединения
cur.close()
conn.close()
print("Соединение закрыто")
