import mysql.connector
from mysql.connector import Error

def main():
    try:
        # Устанавливаем соединение с базой данных
        connection = mysql.connector.connect(
            host='localhost',
            user='second',      # замените на ваше имя пользователя
            password='15032009sg2009',  # замените на ваш пароль
            database='first'
        )

        if connection.is_connected():
            print("Соединение с базой данных установлено")

            cursor = connection.cursor()

            # Создаём таблицу (если её ещё нет)
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            );
            """
            cursor.execute(create_table_query)
            print("Таблица 'users' готова к работе.")

            # Вставляем данные в таблицу
            insert_query = "INSERT INTO users (name) VALUES (%s)"
            user_data = ("Alice",)
            cursor.execute(insert_query, user_data)
            connection.commit()  # сохраняем изменения
            print("Новая запись добавлена.")

            # Выбираем данные из таблицы
            select_query = "SELECT id, name FROM users"
            cursor.execute(select_query)
            records = cursor.fetchall()
            print("Данные из таблицы 'users':")
            for row in records:
                print(f"ID: {row[0]}, Name: {row[1]}")

    except Error as e:
        print("Ошибка при работе с MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Соединение с MySQL закрыто")

if __name__ == "__main__":
    main()