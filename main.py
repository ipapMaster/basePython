# Регулярные выражения
# Regular Expression

import re

pattern = r'начать!\Z'  # на что заканчивается
testString = 'Главное в любом деле - начать!'

result = re.findall(pattern, testString)
print(result)
# print('Цифры присутствуют в строке') if result else print('Цифр нет!')
