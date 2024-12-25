import os
import time
import random
from threading import Thread
import psutil


output_dir = "output_files"
os.makedirs(output_dir, exist_ok=True)


def create_file(index):
    file_name = os.path.join(output_dir, f"file_{index}.txt")
    time.sleep(1)  
    with open(file_name, "w") as file:
        file.write(str(random.randint(1, 100)))


def single_thread_execution():
    start_time = time.time()
    for i in range(100):
        create_file(i)
    print("Single-thread execution time:", time.time() - start_time)


def multithread_execution():
    start_time = time.time()
    threads = []
    for i in range(100):
        thread = Thread(target=create_file, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print("Multithread execution time:", time.time() - start_time)

    print("CPU load during execution:", psutil.cpu_percent(interval=1))

if __name__ == "__main__":
    print("Running single-thread execution...")
    single_thread_execution()

    print("\nRunning multithread execution...")
    multithread_execution()

