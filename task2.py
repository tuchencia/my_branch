import pulp

# Данные из задания
supply = [300, 250, 200] # Запасы на A1, A2, A3
demand = [210, 150, 120, 135, 135] # Потребности на B1, B2, B3, B4, B5
costs = [
    [4, 8, 13, 2, 7],   # Затраты от A1 до B1-B5
    [9, 4, 11, 9, 17],  # Затраты от A2 до B1-B5
    [3, 16, 10, 1, 4]   # Затраты от A3 до B1-B5
]

problem = pulp.LpProblem("Transportation_Problem", pulp.LpMinimize)

# Переменные решения: количество груза от Ai к Bj
x = pulp.LpVariable.dicts("x", (range(3), range(5)), lowBound=0)

problem += pulp.lpSum(costs[i][j] * x[i][j] for i in range(3) for j in range(5))

for i in range(3):
    problem += pulp.lpSum(x[i][j] for j in range(5)) <= supply[i]

for j in range(5):
    problem += pulp.lpSum(x[i][j] for i in range(3)) >= demand[j]

problem.solve()

for i in range(3):
    for j in range(5):
        print(f"Количество груза от A{i+1} к B{j+1}: {x[i][j].varValue} тонн")

print("Минимальные затраты:", pulp.value(problem.objective))