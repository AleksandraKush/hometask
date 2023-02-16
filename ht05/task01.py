"""
Задача возвести число в степень с помощью рекурсии.

"""


def find_power(a, b):
    if (b == 1):
        return (a)
    else:
        return (a * find_power(a, b - 1))

a = int(input("Введите число A: "))
b = int(input("Введите степень B: "))
print(f'Результат: {find_power(a, b)}')