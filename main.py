temperature = 39.9  # запятая недопустима при float

string = 'Температура - ' + str(temperature)
string += ', это почти ' + str(int(temperature) + 1)

print(string)

# Температура - 39.7, это почти 40.

# str(X) - преобразование X в строку
# int(X) - преобразование X в целое
# float(X) - преобразование X в десятичную дробь
