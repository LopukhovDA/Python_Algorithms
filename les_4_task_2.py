"""
Задача 2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее
простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""

import timeit as tit
import cProfile

# Модифицируем алгоритм "Решето Эратосфена"


def simple(num):
    size = num ** 2 + 5
    array = [i for i in range(size)]

    array[1] = 0
    for i in range(2, size):
        if array[i] != 0:
            j = i ** 2
            while j < size:
                array[j] = 0
                j += i

    result = [i for i in array if i != 0]
    return result[num - 1]


def test_simple(func):
    simple_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                   101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                   199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                   317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
                   443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
                   577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                   701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
                   839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977,
                   983, 991, 997, 1009, 1013]

    for i, item in enumerate(simple_nums, start=1):
        assert func(i) == item, f'Test {i} fail\t func({i}) = {func(i)}'
        print(f'Test {i} OK')


# test_simple(simple)  # проверка пройдена


print(tit.timeit('simple(10)', number=1000, globals=globals()))  # 0.07121903800000001
print(tit.timeit('simple(50)', number=1000, globals=globals()))  # 1.451735663
# print(tit.timeit('simple(250)', number=1000, globals=globals()))  # 40.672802455

cProfile.run('simple(50)')
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 les_4_task_2.py:20(simple)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:22(<listcomp>)
        1    0.000    0.000    0.000    0.000 les_4_task_2.py:32(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# рассмотрим простейший алгоритм поиска простого числа


def s_test(numb):
    for i in range(2, numb):
        if numb % i == 0:
            return False
    return True


def simple_h(num):
    result = [i for i in range(num ** 2 + 5) if s_test(i) is True]
    return result[num+1]


# test_simple(simple_h) # проверка пройдена

print(tit.timeit('simple_h(10)', number=1000, globals=globals()))  # 0.2142764610000003
# print(tit.timeit('simple_h(50)', number=1000, globals=globals()))  # 52.631206485
# print(tit.timeit('simple_h(100)', number=1000, globals=globals()))  # 877.349675882

cProfile.run('simple_h(50)')

"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.076    0.076 <string>:1(<module>)
     2505    0.064    0.000    0.064    0.000 les_4_task_2.py:71(s_test)
        1    0.000    0.000    0.076    0.076 les_4_task_2.py:78(simple_h)
        1    0.012    0.012    0.076    0.076 les_4_task_2.py:79(<listcomp>)
        1    0.000    0.000    0.076    0.076 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Алгоритм без использования просеивания работает очень медленно, требует доработки!
