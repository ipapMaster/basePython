# RAM - Random Access Memory (ОЗУ)
# SSD - Solid State Drive (Flash Memory, ПЗУ)
# filename + .ext - расширение
# режим(mode) - w (write) - файл либо создаётся,
# либо в нём все стирается и пишется заново
# a (append) - дописывается (если не существовал, создаётся)
line = ''

f = open('info.txt', 'rt', encoding='utf-8')
for _ in range(3):
    line += f.readline()  # построчное чтение 3х строк
print(line)
f.close()
