import matplotlib.pyplot as plt
import numpy as np

# Данные для графика
queries = np.arange(1, 11)  # Количество запросов от 1 до 10
before_z_ordering = [50, 48, 47, 46, 45, 44, 43, 42, 41, 40]  # Время выполнения до оптимизации (в секундах)
after_z_ordering = [30, 28, 27, 26, 25, 24, 23, 22, 21, 20]  # Время выполнения после Z-Ordering (в секундах)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(queries, before_z_ordering, label='До Z-Ordering', marker='o')
plt.plot(queries, after_z_ordering, label='После Z-Ordering', marker='o')

plt.xlabel('Количество запросов')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Прирост скорости выполнения запросов после использования Z-Ordering')
plt.legend()
plt.grid(True)
plt.show()