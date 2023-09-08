# Регулярные выражения
# Regular Expression

import re

# Квантификаторы (quantifier)
# m - минимальное число совпадений
# n - максимальное число совпадений
# {m} - ровно m раз
# {m,} - m раз и более
# {,n} - не более n раз
# {m, n} - от m до n раз

# Версия написания Google c 3 'o' и более
pattern = 'Go{3,}gle'  # в скобках пишется без пробела
testString = 'Google, Gooogle, Goooooooogle'

result = re.findall(pattern, testString, re.I)  # игнорируем регистр
print(result)
# print('Цифры присутствуют в строке') if result else print('Цифр нет!')
