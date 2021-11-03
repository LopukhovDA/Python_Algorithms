"""
Задача 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random as rnd

# сгенерируем случайный список целых чисел

SIZE = 100
MIN_ITEM = -1000
MAX_ITEM = 1000

numbers = [rnd.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# решим задачу

max_neg = float("-inf")  # минус бесконечность
max_neg_index = 0
for i in range(len(numbers)):
    if numbers[i] < 0:
        if numbers[i] > max_neg:
            max_neg = numbers[i]
            max_neg_index = i

print(numbers)
print(f'Максимальный отрицательный элемент равен {max_neg}, его позиция в массиве: {max_neg_index}')
