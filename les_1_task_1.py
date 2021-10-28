"""
Задача 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
Ссылка на блок-схему:
https://drive.google.com/file/d/1KiJ4IjknkppkubTc5wQNkOTzelrS73CS/view?usp=sharing
"""

x = int(input('Введите целое положительное трехзначное число: '))
c = x % 10
b = int((x - c) / 10 % 10)
a = int((x - 10 * b - c) / 100)
s = a + b + c
m = a * b * c
print(f'Сумма цифр: {s}\n'
      f'Произведение цифр: {m}')
