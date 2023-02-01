# Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзачное число: '))
if number < 1000 and number > 99:
    print(int(number / 100) + int(number % 10) + int(number % 100 / 10))
else: print("это не трехзначное число")