import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def gaussian_quadrature(f_str, a, b):
    """Метод Гаусса для вычисления определенного интеграла"""
    f = eval("lambda x: " + f_str)
    integral, _ = quad(f, a, b)  # Используем встроенный метод scipy для интеграции
    return integral

def plot_gaussian_quadrature(f_str, a, b):
    """График функции с областью под кривой для метода Гаусса"""
    f = eval("lambda x: " + f_str)
    # Вычисление интеграла методом Гаусса
    integral_gaussian = gaussian_quadrature(f_str, a, b)
    print(f"Определенный интеграл методом Гаусса: {integral_gaussian}")
    # Построение графика функции
    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = f(x_vals)
    plt.figure(figsize=(12, 8))
    plt.plot(x_vals, y_vals, label='f(x)', color='black')
    x_fill = np.linspace(a, b, 400)
    y_fill = f(x_fill)
    plt.fill_between(x_fill, y_fill, color='lightblue', alpha=0.5)
    plt.title(f'Метод Гаусса\nПлощадь - {integral_gaussian}', color='blue')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()

function_str = "x**3"  # Задание функции
a = 1   # Начало интервала
b = 4   # Конец интервала
plot_gaussian_quadrature(function_str, a, b)