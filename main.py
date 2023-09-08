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
# . - любой символ
# * - от нуля до "бесконечности" (32767) - {0,}
# ? - от единицы до "бесконечности" (32767) - {1,}
# https://regex101.com/
# в html-документе "вытащить" url из тега ссылки
pattern = r'href=[\'"]?([^\'">]+)'
testString = '<a href="http://ya.ru">Яндекс</a>'

result = re.findall(pattern, testString)
print(result)
# print('Цифры присутствуют в строке') if result else print('Цифр нет!')
