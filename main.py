# Работа с БД PostgreSQL
# pip install psycopg2
import psycopg2 as db

# Соединение
connection = db.connect(host='localhost',
                        port=5500,
                        user='postgres',
                        password='123',
                        dbname='biblio')
# Курсор
cursor = connection.cursor()

query = "SELECT * FROM genre"
cursor.execute(query)
result = cursor.fetchall()

print(result[1][0])

# Отключаем курсор
cursor.close()

# Отключаемся от БД
connection.close()