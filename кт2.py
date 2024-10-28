import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Установка семени генератора случайных чисел для воспроизводимости
np.random.seed(42)

# Генерация данных
x_values = np.linspace(0, 10, 100)
y_values = np.cos(x_values) + np.random.normal(0, 0.4, 100)

# Категории и их значения для круговой диаграммы
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
data_values = np.random.randint(10, 100, size=4)

# Создание графиков
plt.figure(figsize=(14, 10))

# Линейный график
plt.subplot(2, 2, 1)
plt.plot(x_values, np.cos(x_values), label='Косинусоида', color='orange', linewidth=2)
plt.scatter(x_values, y_values, color='magenta', s=15, alpha=0.6, label='Шум')
plt.title('Линейный график')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.legend()

# Гистограмма
plt.subplot(2, 2, 2)
plt.hist(y_values, bins=15, color='cyan', edgecolor='black', alpha=0.7)
plt.title('Гистограмма значений')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.axvline(np.mean(y_values), color='red', linestyle='dashed', linewidth=1)

# График разброса
plt.subplot(2, 2, 3)
plt.scatter(x_values, y_values, color='teal', alpha=0.7, edgecolors='k')
plt.title('График разброса')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)

# Круговая диаграмма
plt.subplot(2, 2, 4)
plt.pie(data_values, labels=categories, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Круговая диаграмма распределения')

# Настройка макета
plt.tight_layout()
plt.show()
