# Функции
def greeting(name='', surname='', age=0, sex=''):
    # local scope
    string = 'Привет, ' + str(name) + ' ' + str(surname) + '!'
    if age != 0:
        string += '\nТебе ' + str(age) + ' лет!'
    if sex:
        string += '\nПол ' + sex
    return string


def incr():
    # local scope
    global num
    num += 1
    return num


def even_or_odd(number):
    if number % 2 == 0:
        return 'Чётное'
    return 'Нечётное'


# global scope
num = 7  # глобальная переменная
print(even_or_odd(num))

