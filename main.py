# Исключения
# Модули и их применение
# Утверждение (Assertion)
try:
    text = input('Введите любой текст: ')
    assert len(text) > 3  # утверждение
except AssertionError:
    print('Длина текста меньше 3-х символов')
