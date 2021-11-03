"""
Задача 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
(индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random as rnd

# сгенерируем случайный список целых чисел

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 10000

numbers = [rnd.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# решим задачу

res_indexes = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        res_indexes.append(i)

print(numbers)
print(res_indexes)
