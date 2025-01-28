import sys
import requests
import json
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QListWidget, QTextEdit, QVBoxLayout, QWidget
)


class UserApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Info Viewer")
        self.setGeometry(100, 100, 600, 400)

        # Основной виджет и макет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Виджеты для списка пользователей и отображения деталей
        self.user_list = QListWidget()
        self.user_details = QTextEdit()
        self.user_details.setReadOnly(True)

        # Добавление виджетов в макет
        layout.addWidget(self.user_list)
        layout.addWidget(self.user_details)

        # Загрузка данных о пользователях
        self.users = []
        self.load_users()

        # Связывание событий
        self.user_list.itemClicked.connect(self.display_user_details)

    def load_users(self):
        """Загрузка данных пользователей с JSONPlaceholder."""
        try:
            response = requests.get("https://jsonplaceholder.typicode.com/users")
            response.raise_for_status()  # Проверка на ошибки
            self.users = response.json()

            # Сохранение данных в JSON-файл
            with open("users.json", "w", encoding="utf-8") as file:
                json.dump(self.users, file, ensure_ascii=False, indent=4)

            self.populate_user_list()
        except requests.RequestException as e:
            self.user_details.setText(f"Ошибка загрузки данных: {e}")
        except IOError as e:
            self.user_details.setText(f"Ошибка записи в файл: {e}")

    def populate_user_list(self):
        """Заполнение списка пользователей."""
        for user in self.users:
            self.user_list.addItem(user["name"])

    def display_user_details(self, item):
        """Отображение информации о выбранном пользователе."""
        user_name = item.text()
        user = next((u for u in self.users if u["name"] == user_name), None)
        if user:
            details = (
                f"Имя: {user['name']}\n"
                f"Почта: {user['email']}\n"
                f"Телефон: {user['phone']}\n"
                f"Вебсайт: {user['website']}\n"
                f"Компания: {user['company']['name']}\n"
                f"Адрес: {user['address']['street']}, {user['address']['city']}"
            )
            self.user_details.setText(details)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserApp()
    window.show()
    sys.exit(app.exec())
