import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Генерация данных
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.5, 100)
categories = ['A', 'B', 'C', 'D']
values = np.random.randint(1, 100, size=4)

# Линейный график
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x), label='Синусоида', color='blue')
plt.scatter(x, y, color='red', s=10, alpha=0.5, label='Шум')
plt.title('Линейный график')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Гистограмма
plt.subplot(2, 2, 2)
plt.hist(y, bins=20, color='green', edgecolor='black')
plt.title('Гистограмма')
plt.xlabel('Значения')
plt.ylabel('Частота')

# График разброса
plt.subplot(2, 2, 3)
plt.scatter(x, y, color='purple', alpha=0.6)
plt.title('График разброса')
plt.xlabel('x')
plt.ylabel('y')

# Круговая диаграмма
plt.subplot(2, 2, 4)
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Круговая диаграмма')

plt.tight_layout()
plt.show()

