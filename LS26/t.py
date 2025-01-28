import tkinter as tk
from tkinter import messagebox
import requests
import json
import os


class JSONPlaceholderClientApp:
    def __init__(self, master):
        self.master = master
        self.master.title("JSONPlaceholder Client")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Введите ID:").pack(pady=5)

        self.entry_id = tk.Entry(self.master)
        self.entry_id.pack(pady=5)

        self.btn_fetch = tk.Button(self.master, text="Получить данные", command=self.fetch_data)
        self.btn_fetch.pack(pady=5)

        self.text_result = tk.Text(self.master, width=50, height=15)
        self.text_result.pack(pady=5)

        self.btn_save = tk.Button(self.master, text="Сохранить в файл", command=self.save_data)
        self.btn_save.pack(pady=5)

    def fetch_data(self):
        user_id = self.entry_id.get()
        if not user_id.isdigit():
            messagebox.showerror("Ошибка", "ID должен быть числом!")
            return

        url = f"https://jsonplaceholder.typicode.com/posts/{user_id}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.text_result.delete("1.0", tk.END)
                self.text_result.insert(tk.END, json.dumps(data, indent=4))
            else:
                messagebox.showerror("Ошибка", f"Данные с ID {user_id} не найдены!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка запроса: {e}")

    def save_data(self):
        data = self.text_result.get("1.0", tk.END).strip()
        if not data:
            messagebox.showerror("Ошибка", "Нет данных для сохранения!")
            return

        folder = "saved_data"
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, "data.json")
        with open(file_path, "w") as f:
            f.write(data)

        messagebox.showinfo("Успех", f"Данные сохранены в {file_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = JSONPlaceholderClientApp(root)
    root.mainloop()
