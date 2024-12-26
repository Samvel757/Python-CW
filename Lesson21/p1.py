import asyncio
import requests
import time


URLS = ["https://jsonplaceholder.typicode.com/posts"] * 100


async def fetch_url_async(url):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, requests.get, url)


async def asynchronous_execution():
    start_time = time.time()
    tasks = [fetch_url_async(url) for url in URLS]  
    responses = await asyncio.gather(*tasks)  
    duration = time.time() - start_time
    print(f"Асинхронное выполнение заняло: {duration:.2f} секунд")
    print(f"Количество успешных ответов: {sum(1 for r in responses if r.status_code == 200)}")


if __name__ == "__main__":
    print("\nАсинхронное выполнение:")
    asyncio.run(asynchronous_execution())