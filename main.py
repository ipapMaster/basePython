# Рекурсия на примере факториала

def power(a, b):
    return a ** b


def factorial(x):
    if x == 1:
        return x
    return x * factorial(x - 1)


lst = ['Иван', 'Пётр', 'Сидор']
lst.sort(key=lambda e: e[2])

lst2 = map(lambda a: 'Привет, ' + a + '!!!', lst)

print(lst)
print(list(lst2))
print(factorial(5))
