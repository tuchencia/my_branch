import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из Excel
try:
    data = pd.read_excel('Datamodel.xlsx')  # Убедитесь, что файл находится в той же директории
except FileNotFoundError:
    print("Файл 'Datamodel.xlsx' не найден.")
    exit()

# Проверка структуры данных
required_columns = ['Угол атаки (градусы)', 'C_d', 'C_l', 'Площадь (м²)', 'Плотность (кг/м³)', 'Коэффициент момента (C_m)', 'Длина (м)']
if not all(col in data.columns for col in required_columns):
    print(f"Файл должен содержать следующие столбцы: {', '.join(required_columns)}")
    exit()

# Извлечение данных
angles = data['Угол атаки (градусы)']
Cd = data['C_d']
Cl = data['C_l']
A = data['Площадь (м²)'].iloc[0]         # Площадь фронтальной проекции (м²)
rho = data['Плотность (кг/м³)'].iloc[0]   # Плотность воздуха (кг/м³)
C_m = data['Коэффициент момента (C_m)'].iloc[0] # Коэффициент момента
L = data['Длина (м)'].iloc[0]             # Длина автомобиля (м)

v_mps = np.linspace(0, 40, num=100)       # Скорость автомобиля в м/с

# Вычисление сил и моментов для каждого угла атаки
Fd_list = []  # Список для хранения значений силы сопротивления
Fl_list = []  # Список для хранения значений подъемной силы
M_list = []   # Список для хранения значений аэродинамических моментов

for i in range(len(angles)):
    Fd = (1 / 2) * Cd[i] * rho * A * v_mps**2   # Сила лобового сопротивления
    Fl = (1 / 2) * Cl[i] * rho * A * v_mps**2   # Подъемная сила
    M = C_m * Fd * L * Fl                            # Аэродинамический момент

    Fd_list.append(Fd)
    Fl_list.append(Fl)
    M_list.append(M)

# Построение графиков силы лобового сопротивления
plt.figure(figsize=(12, 8))
for i in range(len(angles)):
    plt.plot(v_mps, Fd_list[i], label=f'Cd при угле {angles[i]}°')

plt.title('Сила лобового сопротивления в зависимости от скорости')
plt.xlabel('Скорость (м/с)')
plt.ylabel('Сила лобового сопротивления (Н)')
plt.legend()
plt.grid()
plt.show()

# Построение графиков подъемной силы
plt.figure(figsize=(12, 8))
for i in range(len(angles)):
    plt.plot(v_mps, Fl_list[i], label=f'Cl при угле {angles[i]}°')

plt.title('Подъемная сила в зависимости от скорости')
plt.xlabel('Скорость (м/с)')
plt.ylabel('Подъемная сила (Н)')
plt.legend()
plt.grid()
plt.show()

# Построение графиков аэродинамических моментов
plt.figure(figsize=(12, 8))
for i in range(len(angles)):
    plt.plot(v_mps, M_list[i], label=f'M при угле {angles[i]}°')

plt.title('Аэродинамические моменты в зависимости от скорости')
plt.xlabel('Скорость (м/с)')
plt.ylabel('Аэродинамический момент (Н·м)')
plt.legend()
plt.grid()
plt.show()
