# Словари (dictionary)
# key - value

d = {
    'блюдо': 'окрошка',
    'состав': ['квас', 'яйцо', 'огурец', 'колбаса']
}

for item in d:
    if isinstance(d[item], list):
        print(item, end=':\n')
        counter = 1
        for v in d[item]:
            print('\t' + str(counter) + '.', v)
            counter += 1
    else:
        print(item, d[item], sep=': ')
