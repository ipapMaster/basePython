# ДЗ - обучаемый словарь
d = {
    'стол': 'table',
    'стул': 'chair'
}

while True:
    word = input('Введите слово на русском или q - для выхода: ')
    if word == 'q' or word == 'Q':
        break
    if word in d.keys():
        print('Перевод слова', word, '-', d.get(word))
    else:
        transl = input('Этот перевод я не знаю, введите и я его запомню: ')
        d[word] = transl
print('До свидания!')
