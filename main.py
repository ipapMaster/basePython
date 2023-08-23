# Словари (dictionary)
# key - value
# ключи будут 1. блюдо, 2. состав
d = {
    'блюдо': 'окрошка',
    'состав': ['квас', 'яйцо', 'огурец', 'колбаса'],
    'кот': 'Барсик',
    'кушает': ['Wiskas', 'Purina']
}

for item in d:  # перебор словаря по ключам
    if isinstance(d[item], list):
        d[item].sort()  # сортируем список перед выводом
        print(item, end=':\n')
        for index, value in enumerate(d[item]):
            print('\t' + str(index + 1) + '.', value)
    else:
        print(item, d[item], sep=': ')
