"""
Задача 8. Определить, является ли год, который ввел пользователь, високосным или не високосным.
Ссылка на блок-схему:
https://drive.google.com/file/d/1KiJ4IjknkppkubTc5wQNkOTzelrS73CS/view?usp=sharing
"""

year = int(input('Введите год: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Год високосный")
        else:
            print("Год не високосный")
    else:
        print("Год високосный")
else:
    print("Год не високосный")
