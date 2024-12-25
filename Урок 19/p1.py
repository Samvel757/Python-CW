import os
import time
from threading import Thread


def create_file(filename):
    time.sleep(1)
    with open(filename, "w") as f:
        f.write("Файл создан\n")


def sequential_execution():
    start_time = time.time()
    for i in range(100):
        create_file(f"file_{i}.txt")
    end_time = time.time()
    print(f"Время последовательного выполнения: {end_time - start_time:.2f} секунд")


def threaded_execution():
    start_time = time.time()
    threads = []
    for i in range(100):
        thread = Thread(target=create_file, args=(f"file_{i}.txt",))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Время многопоточного выполнения: {end_time - start_time:.2f} секунд")

if name == "main":
    if not os.path.exists("files"):
        os.mkdir("files")
    os.chdir("files")

    print("Последовательное выполнение:")
    sequential_execution()

    print("\nМногопоточное выполнение:")
    threaded_execution()