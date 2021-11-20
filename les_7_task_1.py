"""
Задача 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный
случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

numbers = [random.randint(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]

"""
доработаем код, написанный на уроке. Завернем в функцию и добавим логики чтобы прогон на сравнение
останавливался когда массив у нас уже отсортирован (признак отсортированности - когда мы не передвигаем значения)
"""


def sort_bubble(base_array):
    array = base_array.copy()
    n = 1
    while n < len(array):
        flag_shuffle = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag_shuffle = True
        n += 1
        if flag_shuffle is False:
            return array


print(numbers)
sort_numbers = sort_bubble(numbers)
print(sort_numbers)
print('Test OK' if sorted(numbers) == sort_numbers else 'Test failed')
