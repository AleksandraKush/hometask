list = [10, 6, 4, -3, 7, 2, -5, 4, -2]
min_num = int(input('введите начало диапазона'))
max_num = int(input('введите конец диапазона'))
for i in range(len(list)):
    if min_num <= list[i] <= max_num:
        print(i)