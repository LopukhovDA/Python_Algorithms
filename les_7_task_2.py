"""
Задача 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

SIZE = 25
MIN_ITEM = 0
MAX_ITEM = 50

numbers = [random.uniform(MIN_ITEM, MAX_ITEM - 10 ** (-14)) for _ in range(SIZE)]


def sort_merge(array):
    if len(array) == 1:
        return array

    idx = len(array) // 2
    left_part = array[:idx]
    right_part = array[idx:]
    left = sort_merge(left_part)
    right = sort_merge(right_part)

    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:] + right[j:])
    return result


print(numbers)
sort_numbers = sort_merge(numbers)
print(sort_numbers)
print('Test OK' if sorted(numbers) == sort_numbers else 'Test failed')
