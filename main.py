# Методы строк
# strip
# split
# join
# count

s = 'телевизор'
f = 'а'

if f in s:
    print('Буква', f, 'есть в слове', s)
    print('И она встречается', s.count(f), 'раз(а).')
else:
    print('Буквы', f, 'в слове', s, 'нет!')
