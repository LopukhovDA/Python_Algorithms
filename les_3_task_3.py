"""
Задача 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
"""

import random as rnd

# сгенерируем случайный список целых чисел

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 10000

numbers = [rnd.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# решим задачу

# алгоритм поиска min и max

min_pos = 0
max_pos = 0
min_ = numbers[0]
max_ = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] < min_:
        min_ = numbers[i]
        min_pos = i
    elif numbers[i] > max_:
        max_ = numbers[i]
        max_pos = i

# выведем исходный список
print(numbers)
print(f'Минимальное число - {min_} с позицией {min_pos}\nМаксимальное число - {max_} с позицией {max_pos}')

# поменяем местами
numbers[min_pos], numbers[max_pos] = numbers[max_pos], numbers[min_pos]

# выведем получившийся список
print(numbers)
