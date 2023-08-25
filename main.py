# Анонимная функция (lambda)

def power(a, b):
    return a ** b


lst = ['Иван', 'Пётр', 'Сидор']
lst.sort(key=lambda e: e[2])

lst2 = map(lambda a: 'Привет, ' + a + '!!!', lst)

print(lst)
print(list(lst2))
