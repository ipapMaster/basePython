# Строки
# Исключения
# Модули и их применение
# Поиск в строке (-1 - если ничего не найдено)
# Метод find(substr, start=0, end=None)

string = 'Видеть, вертеть, смотреть'

length = len(string)

if string.find('еть') != -1:  # if 'еть' in string
    count = string.count('еть')

    print('"еть" встречается', count, 'раз(а):')

    index = string.find('еть')  # с самого начала
    print(index)

    index = string.find('еть', index + 1)  # с некоего индекса
    print(index)

    index = string.find('еть', index + 1, length)  # с некоего индекса по конечный индекс
    print(index)
