import os
import aiohttp
import asyncio
import json

url = "https://jsonplaceholder.typicode.com/posts"


async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def save_data():
    data = await fetch_data()
    
    
    folder_name = "json_files_aiohttp"
    os.makedirs(folder_name, exist_ok=True)
    
    for item in data:
        file_path = os.path.join(folder_name, f"{item['id']}.json")
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(item, file)
    
    print(f"JSON-объекты сохранены в папке: {folder_name}")

asyncio.run(save_data())