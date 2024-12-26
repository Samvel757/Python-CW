import os
import random
import time
from multiprocessing import Pool


def create_file(index):
    time.sleep(1)
    file_name = f"file_{index}.txt"
    with open(file_name, "w") as f:
        f.write(str(random.randint(1, 100)))
    return f"Created {file_name}"


def main():
    num_files = 100

    
    start_time = time.time()
    for i in range(num_files):
        create_file(i)
    sequential_duration = time.time() - start_time
    print(f"Последовательное выполнение заняло: {sequential_duration:.2f} секунд")

   
    start_time = time.time()
    with Pool(processes=10) as pool:  
        pool.map(create_file, range(num_files))
    parallel_duration = time.time() - start_time
    print(f"Параллельное выполнение заняло: {parallel_duration:.2f} секунд")

    for i in range(num_files):
        try:
            os.remove(f"file_{i}.txt")
        except FileNotFoundError:
            pass
    print("Созданные файлы были удалены.")

if __name__ == "__main__":
    main()
