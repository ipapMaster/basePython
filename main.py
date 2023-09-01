# Модули и их применение
import requests

key = 'c747bf84924be997ff13ac5034fa3f86'
city = input('Введите город: ')

# ссылка, с которой мы получим все данные в формате JSON
url = 'http://api.openweathermap.org/data/2.5/weather'
# Дополнительные парамтеры (Ключ, город введенный пользователем и единицины измерения - metric означает Цельсий)
params = {'APPID': key, 'q': city, 'units': 'metric'}

result = requests.get(url, params=params)
res = result.json()
# print(res)
print('Температура:', res['main']['temp'], '°C')
print('Реально ощущается как:', res['main']['feels_like'], '°C')
