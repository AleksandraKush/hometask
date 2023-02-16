def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)


a = int(input("Введите первое неотрицательное число: "))
b = int(input("Введите второе нетрицательное число: "))

if a <= 0 or b <= 0 and a <= 0 and b <= 0:
    print(f'Вы ввели отрицательные числа')
else:
    print(f'Сумма ваших чисел равна {sum(a, b)}')