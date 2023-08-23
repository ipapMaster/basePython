# Словари (dictionary)
# key - value
# ключи будут 1. блюдо, ...
d = {
    'блюдо': 'dish',
    'состав': 'composition',
    'кот': 'cat',
    'собака': 'dog'
}

print(list(d.keys()))  # список ключей
print(list(d.values()))  # список значений
for key, value in d.items():
    print(key, value, sep='->')
# выясним есть ли слово "кот" среди ключей
if 'кот' in d.keys():  # метод keys - ключи
    print('Кот есть')
if 'cat' in d.values():  # метод values - значения
    print('Cat есть')
