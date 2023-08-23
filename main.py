# Словари (dictionary)
# key - создание с помощью генератора словарей
# используя два списка
keys = ['one', 'two', 'three']
values = ['один', 'два', 'три']

# генерация словаря с помощью zip
d = {k: v for k, v in zip(keys, values)}

print(d)
