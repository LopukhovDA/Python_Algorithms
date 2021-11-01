"""
Задача 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.

Ссылка на блок-схему алгоритма:
https://drive.google.com/file/d/1rxOws9vDlVXyAVH45VVvjO-lCqcqGNWA/view?usp=sharing
"""


# решим задачу с помощью рекурсии

def rec_sum(p):
    if p == 1:
        return p
    else:
        return p + rec_sum(-2 * p)


n = int(input('Введите число элементов в ряде чисел: 1, -0.5, 0.25, -0.125,… \n'))
if n != 0:
    x = 1 / ((-2) ** (n - 1))
    s = rec_sum(x)
else:
    s = 0
print(s)
