# Списки, цикл for

a = ['Первый', 'Второй']
members = 4

for x in (range(members)):
    print(a[x % 2])

print('Расчёт окончен')
