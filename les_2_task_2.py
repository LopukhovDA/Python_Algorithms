"""
Задача 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

Ссылка на блок-схему алгоритма:
https://drive.google.com/file/d/1rxOws9vDlVXyAVH45VVvjO-lCqcqGNWA/view?usp=sharing
"""

n = int(input('Введите натуральное число: '))
even = 0
non_even = 0
while n >= 1:
    a = n % 10
    n = n // 10
    if a % 2 == 0:
        even += 1
    else:
        non_even += 1
print(f'Четных цифр: {even} \nНечетных цифр: {non_even}')
