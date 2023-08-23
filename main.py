# Словари (dictionary)
# key - value

d = {
    'блюдо': 'окрошка',
    'состав': ['квас', 'яйцо', 'огурец', 'колбаса']
}

for item in d:
    if isinstance(d[item], list):
        d[item].sort()
        print(item, end=':\n')
        for i, v in enumerate(d[item]):
            print('\t' + str(i + 1) + '.', v)
    else:
        print(item, d[item], sep=': ')
