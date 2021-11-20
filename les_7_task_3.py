"""
Задача 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""

import random

# from numpy import median  # для проверки работы алгоритмов

SIZE_M = 10
MIN_ITEM = -100
MAX_ITEM = 100

numbers = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M * 2 + 1)]


# Вариант с использованием сортировки. Будем сортировать алгоритмом "гномьей" сортировки


def sort_gnome(base_array):
    array = base_array.copy()
    i = 1
    j = 2
    while i < len(array):
        if array[i - 1] < array[i]:
            i = j
            j += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
            if i == 0:
                i = j
                j += 1
    return array


print(numbers)
sort_numbers = sort_gnome(numbers)
print(sort_numbers)
print('Sort test OK' if sorted(numbers) == sort_numbers else 'Sort test failed')
median_ = sort_numbers[len(sort_numbers) // 2]
print(f'Медиана массива: {median_}')
# print('Median test OK' if median_ == median(numbers) else 'Median test failed')


"""
Вариант без использования сортировки.
Суть алгоритма заключается в переборе элементов массива и подсчете для каждого элемента кол-ва элементов меньше его.
"""


def search_median(array):
    assert len(array) % 2 != 0, 'длина массива должна быть нечетной'
    for i in range(len(array)):
        counter = 0
        for j in range(len(array)):
            if i != j and array[j] < array[i]:
                counter += 1
        if counter == len(array) // 2:
            return array[i]


med = search_median(numbers)
print(f'Медиана массива: {med}')
# print('Median test OK' if med == median(numbers) else 'Median test failed')
