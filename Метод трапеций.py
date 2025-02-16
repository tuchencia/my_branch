import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_method(f, a, b, n):
    x = np.linspace(a, b, n)
    dx = (b - a) / (n - 1)
    return (dx / 2) * (f(x[0]) + 2 * np.sum(f(x[1:-1])) + f(x[-1]))

def plot_trapezoidal_method(f_str, a, b):
    f = eval("lambda x: " + f_str)
    n = 50  # Количество интервалов
    # Вычисление интеграла
    integral_trapezoidal = trapezoidal_method(f, a, b, n)
    print(f"Определенный интеграл методом трапеций: {integral_trapezoidal}")
    x_vals = np.linspace(a - 1, b + 1, 100)
    y_vals = f(x_vals)
    plt.figure(figsize=(12, 8))
    plt.plot(x_vals, y_vals, label='f(x)', color='black')

    # Трапеции
    for i in range(n - 1):
        x_trap = [a + i * (b - a) / n,
                  a + (i + 1) * (b - a) / n]
        y_trap = [f(x_trap[0]), f(x_trap[1])]
        plt.fill_between(x_trap, y_trap[0], y_trap[1], alpha=0.3, color='red')

    plt.title(f'Метод трапеций\nПлощадь - {integral_trapezoidal}', color='blue')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()
function_str = "x**3"  # Задание функции
a = 1   # Начало интервала
b = 4   # Конец интервала

plot_trapezoidal_method(function_str, a, b)