# RAM - Random Access Memory (ОЗУ)
# SSD - Solid State Drive (Flash Memory, ПЗУ)
# filename + .ext - расширение
# режим(mode) - w (write) - файл либо создаётся,
# либо в нём все стирается и пишется заново
# a (append) - дописывается (если не существовал, создаётся)

f = open('info.txt', 'rt', encoding='utf-8')
info = f.read(3)  # без аргумента читает файл от начала и до конца
print('Из файла прочитано:')
print(info)
f.read(12)  # чтение без сохранения в переменную
info = f.read(3)
print('Из файла также прочитано:')
print(info)
f.close()
