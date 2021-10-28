"""
Задача 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
Ссылка на блок-схему:
https://drive.google.com/file/d/1KiJ4IjknkppkubTc5wQNkOTzelrS73CS/view?usp=sharing
"""

char_num = int(input('Введите номер буквы (от 1 до 26): '))
our_char = chr(char_num + 96)
print(f'Искомая буква - {our_char}')
