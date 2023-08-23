# Словари (dictionary)
# key - создание с помощью генератора словарей
# используя два списка
keys = ['one', 'two', 'three']
values = ['один', 'два', 'три']

d = dict()  # создан пустой словарь
l = len(keys)

for i in range(l):
    d[keys[i]] = values[i]

print(d)
