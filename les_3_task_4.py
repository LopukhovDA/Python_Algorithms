"""
Задача 4. Определить, какое число в массиве встречается чаще всего.
"""

import random as rnd

# сгенерируем случайный список целых чисел

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100

numbers = [rnd.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# решим задачу
# сначала создадим словарь где уникальные числа будут являться ключами, а число совпадений - значением ключа.
# Уникальные числа получим с помощью преобразования списка во множество
result = dict()
for x in set(numbers):
    result[x] = 0

for num in result.keys():
    for i in range(len(numbers)):
        if num == numbers[i]:
            result[num] += 1

# теперь в словаре найдем максимальное число совпадений
max_ = 1

for value in result.values():
    if value > max_:
        max_ = value
#
max_nums = []

# определим числа с максимальным количеством совпадений (может быть не одно число)

for key, value in result.items():
    if value == max_:
        max_nums.append(key)

print('Чаще всего встречающиеся числа:')
print(*max_nums)
print(f'Количество повторений: {max_}')
