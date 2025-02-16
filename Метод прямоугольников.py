import numpy as np
import matplotlib.pyplot as plt

def rectangle_method(f, a, b, n):
    x = np.linspace(a, b, n)
    dx = (b - a) / n
    return np.sum(f(x) * dx)

def plot_rectangle_method(f_str, a, b):
    f = eval("lambda x: " + f_str)
    n = 50  # Количество интервалов
    # Вычисление интеграла
    integral_rectangle = rectangle_method(f, a, b, n)
    print(f"Определенный интеграл методом прямоугольников: {integral_rectangle}")
    x_vals = np.linspace(a - 1, b + 1, 100)
    y_vals = f(x_vals)
    plt.figure(figsize=(12, 8))
    plt.plot(x_vals, y_vals, label='f(x)', color='black')

    # Прямоугольники
    for i in range(n):
        x_rect = np.linspace(a + i * (b - a) / n,
                             a + (i + 1) * (b - a) / n,
                             10)
        y_rect = f(x_rect)
        plt.fill_between(x_rect, y_rect, alpha=0.3)
    plt.title(f'Метод прямоугольников\nПлощадь - {integral_rectangle}', color='blue')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()

function_str = "x**3"  # Задание функции
a = 1   # Начало интервала
b = 4   # Конец интервала
plot_rectangle_method(function_str, a, b)