"""
Задача про кусты из Карелии
"""

from random import randint
count = int(input('введите количество кустов на грядке: '))
bush_count = [randint(1, 10) for i in range(count)]
max1 = 0
i = 0
for i in range(1, count -1):
    max2 = bush_count[i] + bush_count[i + 1] + bush_count[i - 1]
    if max2 > max1:
        max1 = max2
        i += 1
print(bush_count)
print(f'мощная система может за раз собрать аж {max1} ягод(ы)')

