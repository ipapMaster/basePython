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

# в html-документе "вытащить", находящееся между <p> и </p>
pattern = r'<p>(.*?)</p>'
testString = '<b>Жирный</b>.<p>Содержимое абзаца</p>.<i>курсив</i>'

result = re.findall(pattern, testString, re.I)  # игнорируем регистр
print(result[0])
# print('Цифры присутствуют в строке') if result else print('Цифр нет!')
