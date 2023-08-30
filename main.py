# RAM - Random Access Memory (ОЗУ)
# SSD - Solid State Drive (Flash Memory, ПЗУ)
# filename + .ext - расширение
# режим(mode) - w (write) - файл создаётся, в нём все
# стирается и пишется заново
# a (append) - дописывается

f = open('info.txt', 'at', encoding='utf-8')
bytes = f.write('Эта информация уже дописана\n')
print('В файл записано', bytes, 'байт.')
f.close()
