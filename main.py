# При наследовании:
# базовый, родительский, суперкласс, super
# производным, дочерним, derived

def shape_info(shape):
    print(f'Фигура - {shape.name}. Площадь = {shape.area()}, Периметр = {shape.perimetr()}')


class Fruit:
    count = 0  # static

    def __init__(self, name='noname', weight=0):
        self.name = name
        self.weight = weight
        Fruit.count += 1

    def get_name(self):
        return self.name

    def set_name(self, newname):
        self.name = newname

    @staticmethod
    def get_count():
        return Fruit.count


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.name = 'Круг'

    def area(self):
        return 3.14 * self.radius ** 2

    def perimetr(self):
        return 2 * 3.14 * self.radius


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimetr(self):
        return (self.a + self.b) * 2


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = 'Квадрат'


class Student:
    def __init__(self, name, university):
        self.name = name
        self.university = university

    # Для print() и str()
    # Вывод читабельной информации об объекте
    def __str__(self):
        return f'{self.name}, {self.university}'

    # Для разработчика (debug) информации о
    # сложном объекте (список объектов или кортеж...)
    def __repr__(self):
        return f'Класс: {self.__class__.__name__}, {self.name}, {self.university}'


class Employee:
    def __init__(self, name, company):
        self.name = name
        self.company = company


class Person:
    def __init__(self, name):
        self.name = name


# создаём экземпляры
student = Student('Bill', 'Oxford'), Student('John', 'Гарвард')

# Работаем с экземплярами
print(student)

