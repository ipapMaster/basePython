# Исключения
# Модули и их применение
print('Считаем остаток от деления числа 10.')

num = input('Введите целое число: ')
at_the_end = ''

try:
    value = int(num)  # Пытаемся преобразовать строку в целое число
    res = 10 % value
except ZeroDivisionError:  # Деление на ноль
    print('На ноль делить нельзя')
    at_the_end = 'Ай-ай-ай'
except ValueError:
    print('Вас просили ввести целое число.')
    print(f'А вот, что ввели Вы: {num}')
    at_the_end = 'Ну как же так!'
except Exception as e:
    print('Вот такое исключение:', e.__class__.__name__)
    at_the_end = 'Ну вот ещё что'
else:
    print(f'Остаток от деления 10 на {value} будет {res}')  # Если исключения не возникало
    at_the_end = 'Спасибо'
finally:
    print(at_the_end)  # Выполняется в любом случае
