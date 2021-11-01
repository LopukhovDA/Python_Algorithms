"""
Задача 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером
32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

Ссылка на блок-схему алгоритма:
https://drive.google.com/file/d/1rxOws9vDlVXyAVH45VVvjO-lCqcqGNWA/view?usp=sharing
"""

char_num = 32
k = 0
res_str = ''
while char_num <= 127:
    res_str += str(char_num) + ' - ' + chr(char_num) + ' '
    k += 1
    char_num += 1
    if k == 10:
        res_str = res_str + '\n'
        k = 0
print(res_str)
