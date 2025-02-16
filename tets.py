import math

print("Задача 1")
a1 = int(input("Введите параметр а1: "))
a2 = int(input("Введите параметр а2: "))
a3 = int(input("Введите параметр а3: "))
b1 = int(input("Введите параметр b1: "))
b2 = int(input("Введите параметр b2: "))
b3 = int(input("Введите параметр b3: "))
c1 = int(input("Введите параметр c1: "))
c2 = int(input("Введите параметр c2: "))
c3 = int(input("Введите параметр c3: "))
cost1 = int(input("Стоимость единицы продукции на А: "))
cost2 = int(input("Стоимость единицы продукции на B: "))

print("Система ограничений:")
print(f"|{a1}x1 + {b1}x2 <= {c1}\n|{a2}x1 + {b2}x2 <= {c2}\n|{a3}x1 + {b3}x2 <= {c3}")
print(f"F = {cost1} * x1 + {cost2} * x2 --> max (x1 >= 0, x2 >= 0 условие неотрицательности)")
x1A = c1/a1
x2A = c1/b1
x1B = c2/a2
x2B = c2/b2
x1C = c3/a3
x2C = c3/b3
fA = math.ceil(cost1*x1A + cost2*x2A)
fB = math.ceil(cost1*x1B + cost2*x2B)
fC = math.ceil(cost1*x1C + cost2*x2C)
print("Максимальная прибыль:")
print(max([fA, fB, fC]))