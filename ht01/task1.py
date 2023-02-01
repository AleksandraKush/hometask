# Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзачное число: '))
if number < 1000 and number > 99:
    print((number // 100) + (number % 10) + (number % 100 // 10))
else: print("это не трехзначное число")