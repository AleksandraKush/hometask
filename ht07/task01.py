text = input('введите фразу: ')
vowel = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
text = text.split()
res = list()
for i in text:
    k = 0
    for j in i:
        if j in vowel:
            k += 1
    res.append(k)

if len(set(res)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')