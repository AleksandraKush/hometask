"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты 
вверх одной и той же стороной. Выведите минимальное количество 
монет, которые нужно перевернуть.
"""
from random import randint
count = int(input('введите число монеток: '))
i = 0
result = 0
while i < count:
    n = randint(0, 1)
    i = i + 1
    if n == 0:
        result = result + 1
print(f'Минимальное количество монет, которые можно перевернуть: {result}')
    

