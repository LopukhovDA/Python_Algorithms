"""
Задача 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел
в диапазоне от 2 до 9.
"""

# создадим список натуральных чисел от 2 до 99

numbers = [i for i in range(2, 100)]

# создадим список натуральных чисел от 2 до 9

digits = [i for i in range(2, 10)]

# создадим результирующий словарь

result = dict()
for i in digits:
    result[i] = 0

# решаем задачу простым перебором и проверкой кратности

for n in numbers:
    for x in digits:
        if n % x == 0:
            result[x] += 1

print(result)

# сделаем красивый вывод результата
for key, value in result.items():
    print(f'{value} чисел в массиве кратны {key}')
