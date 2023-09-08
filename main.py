# Регулярные выражения
# Regular Expression

import re

pattern = r'\d{3}'  # 3 цифры, идущие подряд
testString = 'Для экстренных вызовов - 12'

result = re.findall(pattern, testString)
print(result)
# print('Цифры присутствуют в строке') if result else print('Цифр нет!')
