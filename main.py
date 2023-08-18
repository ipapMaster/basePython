a = list(input('Ввод числа: '))  # 123

for n in a:
    if int(n) % 2 == 0:
        print('Число:', n, 'чётное.')
    else:
        print('Число:', n, 'нечётное.')
