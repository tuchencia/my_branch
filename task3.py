import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def rectangle_method(f, a, b, n):
    """Метод прямоугольников"""
    x = np.linspace(a, b, n)
    dx = (b - a) / n
    return np.sum(f(x) * dx)

def trapezoidal_method(f, a, b, n):
    """Метод трапеций"""
    x = np.linspace(a, b, n)
    dx = (b - a) / (n - 1)
    return (dx / 2) * (f(x[0]) + 2 * np.sum(f(x[1:-1])) + f(x[-1]))

def simpson_method(f, a, b, n):
    """Метод Симпсона"""
    if n % 2 == 1:  # Simpson's rule requires an even number of intervals
        n += 1
    x = np.linspace(a, b, n)
    h = (b - a) / (n - 1)
    return (h / 3) * (f(x[0]) + 4 * np.sum(f(x[1:-1:2])) + 2 * np.sum(f(x[2:-2:2])) + f(x[-1]))

def gaussian_quadrature(f, a, b):
    """Метод Гаусса"""
    return quad(f, a, b)[0]

def plot_integration_methods(f_str, a, b):
    f = eval("lambda x: " + f_str)

    n = 100  # Количество интервалов

    # Определение интегралов
    integral_rectangle = rectangle_method(f, a, b, n)
    integral_trapezoidal = trapezoidal_method(f, a, b, n)
    integral_simpson = simpson_method(f, a, b, n)
    integral_gaussian = gaussian_quadrature(f, a, b)

    print(f"Определенный интеграл методом прямоугольников: {integral_rectangle}")
    print(f"Определенный интеграл методом трапеций: {integral_trapezoidal}")
    print(f"Определенный интеграл методом Симпсона: {integral_simpson}")
    print(f"Определенный интеграл методом Гаусса: {integral_gaussian}")

    # Построение графика функции
    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(12, 8))

    # График функции
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')

    # Прямоугольники
    for i in range(n):
        x_rect = np.linspace(a + i * (b - a) / n,
                             a + (i + 1) * (b - a) / n,
                             10)
        y_rect = f(x_rect)
        plt.fill_between(x_rect, y_rect, alpha=0.3)

    plt.title('Метод прямоугольников')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()

    plt.show()

# Пример использования
function_str = "x**2"  # Задайте функцию здесь
a = -2   # Начало интервала
b = 2   # Конец интервала

plot_integration_methods(function_str, a, b)