import numpy as np
import matplotlib.pyplot as plt
def simpson_method(f, a, b, n):
    if n % 2 == 1:
        n += 1
    x = np.linspace(a, b, n)
    h = (b - a) / (n - 1)
    return (h / 3) * (f(x[0]) +
                      4 * np.sum(f(x[1:-1:2])) +
                      2 * np.sum(f(x[2:-2:2])) +
                      f(x[-1]))

def plot_simpson_method(f_str, a, b):
    f = eval("lambda x: " + f_str)
    n=50
    if n % 2 == 0:
        pass
    else:
        n = n + 1
    # Вычисление интеграла
    integral_simpson = simpson_method(f, a, b, n)
    print(f"Определенный интеграл методом Симпсона: {integral_simpson}")
    # Построение графика функции
    x_vals = np.linspace(a - 1, b + 1, 100)
    y_vals = f(x_vals)
    plt.figure(figsize=(12, 8))
    # График функции
    plt.plot(x_vals, y_vals, label='f(x)', color='black')

    for i in range(0,n-1 ,2):
        x_simpson = [a + i * (b - a) / n,
                    a + (i + 2) * (b - a) / n]
        y_simpson = [f(x_simpson[0]), f((x_simpson[0] + x_simpson[1]) / 2), f(x_simpson[1])]
        plt.fill_between([x_simpson[0], x_simpson[0], x_simpson[1]], [y_simpson[0], y_simpson[2], y_simpson[2]], alpha=0.3)
    plt.title(f'Метод Симпсона\nПлощадь - {integral_simpson}', color='blue')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()

function_str = "x**3"  # Задание функции
a = 1   # Начало интервала
b = 4   # Конец интервала
plot_simpson_method(function_str, a, b)