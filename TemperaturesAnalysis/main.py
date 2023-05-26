#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

# открыть файл со значениями температур за промежуток времени 1tempdata.txt
# найти макс., мин. и среднюю температуры
# найти общее количество значений температур
# найти количество уникальных значений температур
# найти количество повторений для значений температур
# вывести значения температура -- количество повторений, отсортированных по количеству повторений (по возрастанию)
# по запросу пользователя вывести количество значений температур в промежутке [a,b], отсортированных по значению температуры от a к b

temp = [] #list
occur = {} #dict

with open('1tempdata.txt') as infile:
    for row in infile:
        r = float(row.strip())
        temp.append(r)
        occur[r] = occur.get(r, 0) + 1

maxtemp = max(temp)
mintemp = min(temp)
avgtemp = sum(temp)/len(temp)

print('Max temperature: ', maxtemp)
print('Min temperature: ', mintemp)
print('Avg temperature: ', avgtemp)

uniqtemp = set(temp)
print('All temperatures count: ', len(temp))
print('Unique temperatures count: ', len(uniqtemp))

print('Temperatures sorted by value (number of appearances):')
for it in sorted(occur.items(), key = lambda v: v[1]):
    print('temp ', it[0], '\t', it[1])

a = float(input('Input lower bound: ')) #
b = float(input('Input upper bound: '))

print('Temperatures sorted by key (temperature degree):')
for key in sorted(occur): # словарь отсортированный по ключу
    if (a <= key <= b):
        print('temp ', key, '\t', occur[key])