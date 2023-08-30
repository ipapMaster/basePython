# RAM - Random Access Memory (ОЗУ)
# SSD - Solid State Drive (Flash Memory, ПЗУ)
# filename + .ext - расширение
# режим(mode) - w (write) - файл либо создаётся,
# либо в нём все стирается и пишется заново
# a (append) - дописывается (если не существовал, создаётся)
f = open('info.txt', 'wt', encoding='utf-8')
print('Печатаем прямо в файл', file=f)  # печать прямо в файл
f.close()
