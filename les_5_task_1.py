"""
Задача 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

"""
Решим задачу с помощью коллекции "именнованный кортеж", его использование наиболее целесообразно, так как у нас
есть объект (предприятие) и аттрибуты объекта (прибыль за кварталы) 
"""

from collections import namedtuple

QUARTER = 4
Firm = namedtuple('Firm', 'name, profit, total')
firm_count = int(input("Введите количество предприятий: "))
firm = list()
sum_ = 0

for i in range(1, firm_count + 1):
    name_ = input(f'Введите наименование предприятия №{i}: ')
    profit_ = list()
    for k in range(1, QUARTER + 1):
        profit_.append(float(input(f'Введите прибыль за {k}-й квартал: ')))
    total_ = sum(profit_)  # вроде запрета не было sum использовать
    sum_ += total_
    firm.append(Firm(name_, profit_, total_))

# найдем среднюю прибыль всех предприятий за год

average = sum_ / firm_count
print(f'Средняя прибыль всех предприятий за год: {average}')

names_high = list()
names_low = list()
for x in range(firm_count):
    if firm[x].total > average:
        names_high.append(firm[x].name)
    elif firm[x].total < average:
        names_low.append(firm[x].name)

print('Предприятия с прибылью выше средней:')
print(*names_high)
print('*' * 40)
print('Предприятия с прибылью ниже средней:')
print(*names_low)
