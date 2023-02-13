"""
Задаем длину списка наполненного 
рандомными числами от 1 до 100.
Вводим искомое число X
Программа должна вывести в консоль сколько 
раз встречается в заданном списке искомое 
число X,которое мы вводим с клавиатуры, 
либо выводим на экран, максимально близкое 
ему по значению.
"""

from random import randint
count = int(input('введите количество элементов в списке: '))
list = [randint(1, 10) for i in range(count)]
print(list)
x = int(input('введите число Х: '))
result = 0
i = 0
for i in range(len(list)):
    if x == list[i]:
        result += 1
        i += 1
if result == 0:
    b = list[0]
    for item in list:
        if abs(x - item) < abs(x - b):
            b = item
    print(f'максимальное близкое значение к числу {x} - {b}')
else:
    print(f'число {x} встречается в списке {result} раз(а)')