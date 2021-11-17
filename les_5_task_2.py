"""
Задача 2. Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

DEC_NUMS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
            'C': 12, 'D': 13, 'E': 14, 'F': 15}
HEX_NUMS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

hex_first = list(input('Введите первое шестнадцатиричное число: ').upper())
hex_second = list(input('Введите второе шестнадцатиричное число: ').upper())
num_count = max(len(hex_first), len(hex_second))
num_first = deque(hex_first)
num_second = deque(hex_second)

if len(hex_first) > len(hex_second):
    for _ in range(num_count - len(hex_second)):
        num_second.appendleft('0')
elif len(hex_first) < len(hex_second):
    for _ in range(num_count - len(hex_first)):
        num_first.appendleft('0')

result_dec = deque()
transfer = 0
for _ in range(num_count):
    sum_ = DEC_NUMS[num_first.pop()] + DEC_NUMS[num_second.pop()] + transfer
    if sum_ > 15:
        transfer = 1
        sum_ -= 16
    else:
        transfer = 0
    result_dec.appendleft(sum_)
if transfer == 1:
    result_dec.appendleft(1)

result_hex = list()
for _ in range(len(result_dec)):
    result_hex.append(HEX_NUMS[result_dec.popleft()])

print(f'Сумма чисел равна: {"".join(result_hex)}')

# умножение (было по желанию) не делал для экономии времени, сделаю в выходные, могу дополнительно решение скинуть
