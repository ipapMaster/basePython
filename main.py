# Методы строк
# strip
# split
# join
# count

lst = ['божество', 'вдохновенье', 'смех', 'слёзы', 'любовь']

# с помощью join
string = 'И ' + ', и '.join(lst) + '.'
print(string)

# с помощью print
print('И', end=' ')
print(*lst, sep=', и ')
