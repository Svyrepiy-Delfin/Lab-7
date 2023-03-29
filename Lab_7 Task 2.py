import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data1 - data1.csv.csv')

time = data['Время']
dross = data['Положение дроссельной заслонки (%)']

plt.plot(time, dross, label='Положение дроссельной заслонки')

plt.title('Дроссельная заслонка vs обороты двигателя')
plt.xlabel('Время')
plt.ylabel('Условные единицы')

engine = data['Обороты двигателя (об/мин)'] / 100

plt.plot(time, engine, label='Обороты двигателя')

plt.title('Обороты двигателя')
plt.xlabel('Время')
plt.ylabel('Обороты двигателя (об/мин)')

plt.legend()

plt.show()

corr = dross.corr(engine)

plt.scatter(dross, engine)
plt.title(f'Положение дроссельной заслонки vs обороты двигателя (Корреляция: {corr:.2f})')
plt.xlabel('Положение дроссельной заслонки')
plt.ylabel('Обороты двигателя')
plt.show()