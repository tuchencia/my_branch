import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
data = pd.read_excel('Data.xlsx')
X = data[['Осадки', 'Температура', 'Уровень_воды']]  # признаки
y = data['Наводнение']  # целевая переменная (0 - нет наводнения, 1 - есть наводнение)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
years = np.arange(2020, 2031)
precipitation_levels = np.linspace(500, 1000, len(years))
temperature_levels = np.linspace(10, 20, len(years))
water_levels = np.linspace(2, 4, len(years))
future_data = pd.DataFrame({
    'Осадки': precipitation_levels,
    'Температура': temperature_levels,
    'Уровень_воды': water_levels
}, index=years)
probabilities = model.predict_proba(future_data[['Осадки', 'Температура', 'Уровень_воды']])[:, 1]
plt.figure(figsize=(10, 6))
plt.plot(years, probabilities, marker='o')
plt.title('Вероятность наводнений по годам')
plt.xlabel('Год')
plt.ylabel('Вероятность наводнения')
plt.grid(True)
plt.show()
location_probabilities = model.predict_proba(X)[:, 1]
plt.figure(figsize=(10, 6))
plt.scatter(data['Место'], location_probabilities, marker='o', alpha=0.5)
plt.title('Вероятность наводнений по местам')
plt.xlabel('Место')
plt.ylabel('Вероятность наводнения')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.grid(True)
plt.show()
