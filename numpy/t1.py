import numpy as np

sales_data = [120, 85, 90, 150, 200, 170, 130, 95, 100, 110]

mean = np.mean(sales_data)  
median = np.median(sales_data) 
std_dev = np.std(sales_data)  
min_value = np.min(sales_data)  
max_value = np.max(sales_data) 

print(f"Среднее: {mean}")
print(f"Медиана: {median}")
print(f"Стандартное отклонение: {std_dev}")
print(f"Минимум: {min_value}")
print(f"Максимум: {max_value}")