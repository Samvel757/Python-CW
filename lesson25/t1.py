import tkinter as tk
from tkinter import messagebox
import requests
import json
import os


def fetch_data():
    user_id = entry_id.get()
    if not user_id.isdigit():
        messagebox.showerror("Ошибка", "ID должен быть числом!")
        return
    
    url = f"https://jsonplaceholder.typicode.com/posts/{user_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            text_result.delete("1.0", tk.END)  
            text_result.insert(tk.END, json.dumps(data, indent=4))
        else:
            messagebox.showerror("Ошибка", f"Данные с ID {user_id} не найдены!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка запроса: {e}")


def save_data():
    data = text_result.get("1.0", tk.END).strip()
    if not data:
        messagebox.showerror("Ошибка", "Нет данных для сохранения!")
        return
    
    folder = "saved_data"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, "data.json")
    with open(file_path, "w") as f:
        f.write(data)
    
    messagebox.showinfo("Успех", f"Данные сохранены в {file_path}")


window = tk.Tk()
window.title("JSONPlaceholder Client")

tk.Label(window, text="Введите ID:").pack(pady=5)
entry_id = tk.Entry(window)
entry_id.pack(pady=5)

btn_fetch = tk.Button(window, text="Получить данные", command=fetch_data)
btn_fetch.pack(pady=5)

text_result = tk.Text(window, width=50, height=15)
text_result.pack(pady=5)


btn_save = tk.Button(window, text="Сохранить в файл", command=save_data)
btn_save.pack(pady=5)

window.mainloop()