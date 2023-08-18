color = input('Цвет шарика: ')

match color:
    case 'red' | 'blue':
        print('Подходит')
    case _:
        print('Не подходит')
