temperature = 39.8  # запятая недопустима при float
# ASCII 176 - B0 - °
# Unicode 2 байта
# Escape Sequence
string = 'Температура - ' + str(temperature) + '\xB0C'
string += ', это почти ' + str(round(temperature)) + '\xB0C'

print(string)

# Температура - 39.7, это почти 40.

# str(X) - преобразование X в строку
# int(X) - преобразование X в целое
# float(X) - преобразование X в десятичную дробь
