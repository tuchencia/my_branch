import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from scipy.linalg import solve

# Данные задачи
c = [-5.2, -1.4]  # Коэффициенты целевой функции (максимизация прибыли, знак минус для linprog)
A = [[32, 35], [2.3, 4.5], [18.7, 9], [-1, 0], [0, -1]]  # Коэффициенты ограничений
b = [318, 30, 156, -1, -2]  # Ограничения по ресурсам и дополнительные ограничения

# Решение задачи линейного программирования
res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

# Проверка успешности решения
if res.success:
    x1_optimal, x2_optimal = res.x
    max_profit = -res.fun

    print(f"Оптимальное количество продукции P1 (x1): {x1_optimal:.2f}")
    print(f"Оптимальное количество продукции P2 (x2): {x2_optimal:.2f}")
    print(f"Максимальная прибыль: {max_profit:.2f}")
else:
    print("Решение не найдено:", res.message)
    exit()

# Построение графика области допустимых решений
x = np.linspace(0, 20, 200)

# Вычисление ограничений
y1 = (318 - 32 * x) / 35   # Из первого ограничения
y2 = (30 - 2.3 * x) / 4.5    # Из второго ограничения
y3 = (156 - 18.7 * x) / 9   # Из третьего ограничения
y4 = np.full_like(x, 2)      # Ограничение x2 >= 2
y5 = np.full_like(x, np.nan) # Ограничение x1 >= 1

# Установка области допустимых значений (y >= 0)
y1[y1 < 0] = np.nan
y2[y2 < 0] = np.nan
y3[y3 < 0] = np.nan

# Учитываем ограничение x1 >= 1
x_min = max(1, min(x))       # Ограничиваем область по x >= 1

plt.figure(figsize=(10, 8))

# Построение линий ограничений
plt.plot(x, y1, label=r'$32x_1 + 35x_2 \leq 318$', color='blue')
plt.plot(x, y2, label=r'$2.3x_1 + 4.5x_2 \leq 30$', color='green')
plt.plot(x, y3, label=r'$18.7x_1 + 9x_2 \leq 156$', color='red')
plt.axhline(2, label=r'$x_2 \geq 2$', color='purple', linestyle='--')   # Ограничение x2 >= 2
plt.axvline(1, label=r'$x_1 \geq 1$', color='orange', linestyle='--')   # Ограничение x1 >= 1

# Заполнение области допустимых решений
plt.fill_between(x[x >= x_min],
                 np.maximum.reduce([np.zeros_like(x), y4])[x >= x_min],
                 np.minimum.reduce([y1, y2, y3])[x >= x_min],
                 color='gray', alpha=0.3)

# Настройки графика
plt.xlim(0, max(x))
plt.ylim(0, max(np.nanmax(y1), np.nanmax(y2), np.nanmax(y3)) + 10)
plt.xlabel(r'$x_1$ (Продукт P1)')
plt.ylabel(r'$x_2$ (Продукт P2)')
plt.title('Область допустимых решений с учетом ограничений $x_1 \geq 1$, $x_2 \geq 2$')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid()
plt.legend()

# Функция для нахождения точки пересечения двух прямых
def find_intersection(a1, b1, c1, a2, b2, c2):
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    try:
        intersection = solve(A, B)
        return intersection
    except np.linalg.LinAlgError:
        return None

# Нахождение точек пересечения прямых
intersections = []
intersections.append(find_intersection(32, 35, 318, 2.3, 4.5, 30))   # Пересечение первой и второй
intersections.append(find_intersection(32, 35, 318, 18.7, 9, 156))    # Пересечение первой и третьей
intersections.append(find_intersection(2.3, 4.5, 30, 18.7, 9, 156))   # Пересечение второй и третьей

# Отображение точек пересечения на графике
for point in intersections:
    if point is not None:
        plt.scatter(point[0], point[1], color='red', zorder=5)
        plt.text(point[0] + 0.5, point[1] + 0.5,
                 f'({point[0]:.2f}, {point[1]:.2f})',
                 fontsize=10)

# Отображение оптимальной точки на графике
plt.scatter(x1_optimal, x2_optimal, color='black', zorder=6)
plt.text(x1_optimal + 4, x2_optimal + 4,
         f'Оптимальная точка\n({x1_optimal:.2f}, {x2_optimal:.2f})',
         fontsize=10)

# Показ графика
plt.show()

