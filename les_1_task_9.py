"""
Задача 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
Ссылка на блок-схему:
https://drive.google.com/file/d/1KiJ4IjknkppkubTc5wQNkOTzelrS73CS/view?usp=sharing
"""
print('Необходимо ввести три разных числа')
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if ((a > b) and (b > c)) or ((a < b) and (c > b)):
    print(f'Среднее число: {b}')
if ((a < b) and (c < b) and (a > c)) or ((a > b) and (b < c) and (a < c)):
    print(f'Среднее число: {a}')
if ((a < b) and (c < b) and (a < c)) or ((a > b) and (b < c) and (a > c)):
    print(f'Среднее число: {c}')
