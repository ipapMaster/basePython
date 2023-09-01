# Исключения
# Модули и их применение
max_val = 10
min_val = 1

try:
    cur_val = int(input(f'Введите целое число от {min_val} до {max_val}: '))
    if not min_val <= cur_val <= max_val:
        raise ValueError('введённое число вне диапазона')
except ValueError as exp:
    print('Будьте внимательны:', exp)
else:
    print(f'Да. Введенное число лежит в заданном диапазоне: {min_val}...{max_val}')