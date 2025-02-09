import matplotlib.pyplot as plt

months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт']
sales = [120, 85, 90, 150, 200, 170, 130, 95, 100, 110]

plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', label='Продажи')
plt.title('Продажи товаров за 10 месяцев')
plt.xlabel('Месяцы')
plt.ylabel('Продажи (шт.)')
plt.grid(True)
plt.legend()
plt.show()