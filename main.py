# Списки

array = []  # пустой список
array2 = list('Python')  # пустой список через функцию list
array3 = [1, 2, 3, 4, 5]  # аналог маcсива типа int
list_4 = [36.6, 50, 'Температура', True]
index = -1
length = len('Python')
print('Список длиной -', length)
print(list_4[-3])
print(array2)

counter = 0  # счётчик элементов

while counter < len(list_4):
    print(list_4[counter])
    counter += 1

# Срез подчиняется системе sss
# s - start
# s - stop
# s - step

print(list_4[0:len(list_4):2])
