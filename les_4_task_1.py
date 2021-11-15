"""
Задача 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N
вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

Дла анализа взята задача номер 3 из третьего урока:
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
"""

import random as rnd
import timeit as tit
import cProfile

# видоизменим код задачи для удобства анализа

# функция для генерации исходного списка

MIN_ITEM = 0
MAX_ITEM = 10000


def gen_list(size, min_item, max_item):
    spam_list = [rnd.randint(min_item, max_item) for _ in range(size)]
    return spam_list


# функция для алгоритма
# вариант 1 (исходный)

def change_min_max(numbers):
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
    numbers[min_pos], numbers[max_pos] = numbers[max_pos], numbers[min_pos]
    return numbers


nums_100 = gen_list(100, MIN_ITEM, MAX_ITEM)
nums_1000 = gen_list(1000, MIN_ITEM, MAX_ITEM)
nums_10000 = gen_list(10000, MIN_ITEM, MAX_ITEM)
nums_100000 = gen_list(100000, MIN_ITEM, MAX_ITEM)
nums_1000000 = gen_list(1000000, MIN_ITEM, MAX_ITEM)

print(tit.timeit('change_min_max(nums_100)', number=1000, globals=globals()))  # 0.015462655000000325
print(tit.timeit('change_min_max(nums_1000)', number=1000, globals=globals()))  # 0.1829283140000002
print(tit.timeit('change_min_max(nums_10000)', number=1000, globals=globals()))  # 1.9947255290000006
# print(tit.timeit('change_min_max(nums_100000)', number=1000, globals=globals()))  # 18.780173857
# print(tit.timeit('change_min_max(nums_1000000)', number=1000, globals=globals()))  # 191.88707744899997
# последние два не повторять))) поэтому закомментировал

cProfile.run('change_min_max(nums_10000)')

"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.002    0.002    0.002    0.002 les_4_task_1.py:35(change_min_max)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# Вариант 2. С применением встроенных функций min, max, index

def change_f(numbers):
    min_pos = numbers.index(min(numbers))
    max_pos = numbers.index(max(numbers))
    numbers[min_pos], numbers[max_pos] = numbers[max_pos], numbers[min_pos]
    return numbers


print(tit.timeit('change_f(nums_100)', number=1000, globals=globals()))  # 0.017595906999999578
print(tit.timeit('change_f(nums_1000)', number=1000, globals=globals()))  # 0.09210770099999976
print(tit.timeit('change_f(nums_10000)', number=1000, globals=globals()))  # 0.8724008320000003
# print(tit.timeit('change_f(nums_100000)', number=1000, globals=globals()))  # 6.451032237
# print(tit.timeit('change_f(nums_1000000)', number=1000, globals=globals()))  # 63.331862445

cProfile.run('change_f(nums_10000)')

"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 les_4_task_1.py:80(change_f)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""


# вариант 3 с использованием цикла while

def change_w(numbers):
    min_pos = 0
    max_pos = 0
    min_ = numbers[0]
    max_ = numbers[0]
    i = 0

    while i < len(numbers):
        if numbers[i] < min_:
            min_ = numbers[i]
            min_pos = i
        elif numbers[i] > max_:
            max_ = numbers[i]
            max_pos = i
        i += 1
    numbers[min_pos], numbers[max_pos] = numbers[max_pos], numbers[min_pos]
    return numbers


print(tit.timeit('change_w(nums_100)', number=1000, globals=globals()))  # 0.03002684199999983
print(tit.timeit('change_w(nums_1000)', number=1000, globals=globals()))  # 0.35954388299999973
print(tit.timeit('change_w(nums_10000)', number=1000, globals=globals()))  # 3.3950798340000006
# print(tit.timeit('change_w(nums_100000)', number=1000, globals=globals()))  # 34.360723429
# print(tit.timeit('change_w(nums_1000000)', number=1000, globals=globals()))  # 348.86957442

cProfile.run('change_w(nums_10000)')

"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.081    0.081 <string>:1(<module>)
        1    0.042    0.042    0.081    0.081 les_4_task_1.py:109(change_w)
        1    0.000    0.000    0.082    0.082 {built-in method builtins.exec}
    10001    0.039    0.000    0.039    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
Краткие выводы
Во всех трёх вариантах прослеживается линейная зависимость.
Наибольшее быстродействие показал вариант с использованием встроенных функций min и max.
Наихудшие показатели у варианта с использованием цикла while. Также через cProfile в варианте
с циклом while было видно что много раз была вызвана функция len.
Оптимально в данной задаче использование встроенных функций.
"""
