import os
import requests

image_url = "https://i.postimg.cc/XJhS0mMP/hunting-on-waterfall-8k-tiger-uhd-mrurih9t5drqrg3x.jpg"


for i in range(10):
    folder_name = f"image_folder_{i+1}"
    os.makedirs(folder_name, exist_ok=True) 
    response = requests.get(image_url)
    if response.status_code == 200:
        file_path = os.path.join(folder_name, f"image_{i+1}.jpg")
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Сохранено изображение в {file_path}")
        print(f"Картинка успешно добавлена в файл")
    else:
        print(f"Ошибка при скачивании изображения #{i+1}")