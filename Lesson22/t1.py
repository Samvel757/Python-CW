import os
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()

folder_name = "json_files_requests"
os.makedirs(folder_name, exist_ok=True)

for item in data:
    file_path = os.path.join(folder_name, f"{item['id']}.json")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(item))

print(f"JSON-объекты сохранены в папке: {folder_name}")