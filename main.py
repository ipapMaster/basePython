# Регулярные выражения
# Regular Expression

import re

pattern = r'\b\w{4}\b'
testString = 'Мама мыла раму, а папа уехал на пилораму'

result = re.findall(pattern, testString)
print(result)
