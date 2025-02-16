import numpy as np
from scipy.optimize import linprog

# Функция для ввода данных
def input_data():
    m = int(input("Введите количество пунктов отправления: "))
    n = int(input("Введите количество пунктов назначения: "))

    supply = []
    for i in range(m):
        supply.append(int(input(f"Введите запас для пункта отправления A{i + 1}: ")))

    demand = []
    for j in range(n):
        demand.append(int(input(f"Введите потребность для пункта назначения B{j + 1}: ")))

    costs = []
    print("Введите матрицу тарифов (стоимость перевозки):")
    for i in range(m):
        row = list(map(int, input(f"Введите тарифы для A{i + 1} через пробел: ").split()))
        costs.append(row)

    return supply, demand, np.array(costs)

# Функция для решения транспортной задачи
def solve_transport_problem(supply, demand, costs):
    # Проверка закрытости задачи
    if sum(supply) != sum(demand):
        print("Задача преобразована в закрытую модель.")
        if sum(supply) > sum(demand):
            demand.append(sum(supply) - sum(demand))  # Добавляем фиктивного потребителя
            costs = np.hstack((costs, np.zeros((len(supply), 1))))  # Добавляем столбец с нулевыми тарифами
        else:
            supply.append(sum(demand) - sum(supply))  # Добавляем фиктивного поставщика
            costs = np.vstack((costs, np.zeros((1, len(demand)))))  # Добавляем строку с нулевыми тарифами

    # Создаем коэффициенты целевой функции (разворачиваем матрицу тарифов в вектор)
    c = costs.flatten()

    # Создаем ограничения для поставщиков (по строкам)
    A_eq_supply = np.zeros((len(supply), len(supply) * len(demand)))
    for i in range(len(supply)):
        A_eq_supply[i, i * len(demand):(i + 1) * len(demand)] = 1

    # Создаем ограничения для потребителей (по столбцам)
    A_eq_demand = np.zeros((len(demand), len(supply) * len(demand)))
    for j in range(len(demand)):
        A_eq_demand[j, j::len(demand)] = 1

    # Объединяем ограничения
    A_eq = np.vstack([A_eq_supply, A_eq_demand])
    b_eq = np.hstack([supply, demand])

    # Условия неотрицательности
    bounds = [(0, None) for _ in range(len(supply) * len(demand))]

    # Решение линейной задачи с минимизацией затрат
    result = linprog(c=c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

    if result.success:
        print("Задача решена успешно!")
        x_optimal = result.x.reshape(len(supply), len(demand))   # Оптимальный план перевозок
        total_costs = result.fun                                      # Суммарные затраты
        print("Оптимальный план перевозок:")
        print(x_optimal)
        print(f"Суммарные затраты: {total_costs:.2f}")
    else:
        print("Решение не найдено:", result.message)

# Основная программа
if __name__ == "__main__":
    supply, demand, costs = input_data()
    solve_transport_problem(supply, demand, costs)


