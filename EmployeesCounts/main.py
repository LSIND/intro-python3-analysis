#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

# прочитать данные из input.csv - информация о найме сотрудников
# определить количество нанятых сотрудников за каждый день периода
# построить столбчатую диаграмму Ox: дни, Oy: количество сотрудников

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

df = pd.read_csv('empl.csv', delimiter=',')
df['HireDate'] = pd.to_datetime(df.HireDate)
df['HireDate'] = df.HireDate.dt.date
print(df)

sr = pd.Series(df['HireDate'])
#sr.loc['2018-09-01':'2018-09-30']
mask = (sr >= datetime.strptime('2018-09-01', "%Y-%m-%d").date()) & (sr <= datetime.strptime('2018-09-30', "%Y-%m-%d").date())
sr = sr.loc[mask]
freq = sr.value_counts().sort_index()
#print(sr.values)
print(freq)

fig = plt.figure(figsize=(6,6))
ax = freq.plot(kind='bar', color='purple')
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
fig.autofmt_xdate()

plt.grid(True)
plt.show()
