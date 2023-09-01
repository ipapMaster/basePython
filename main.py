# Строки
# Исключения
# Модули и их применение
# Поиск в строке (-1 - если ничего не найдено)
# Метод replace(old, new, count=None)

tv = 'тиливизор'  # телевизор
print(tv.replace('и', 'е', 2))

string = '+7-012-345-67-89'

length = len(string)

# заменяем на открытую скобку
o_braked_phone = string.replace('-', ' (', 1)
print(o_braked_phone)

# заменяем на открытую скобку
c_braked_phone = o_braked_phone.replace('-', ') ', 1)
print(c_braked_phone)
