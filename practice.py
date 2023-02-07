#Задание 16.9.1

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.widht = width
        self.height = height

    def __str__(self):
        return f"Rectangle : {self.x}, {self.y}, {self.widht}, {self.height}"

rect_1 = Rectangle(5,10,50,100)
print(rect_1)

print("-----------")

#Задание 16.9.2

class Rectangle_1:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def Area(self):
        return self.x1 * self.y1
rect_2 = Rectangle_1(3,4)
print("Площадь прямоугольника равна " + str(rect_2.Area()))

print("-----------")

#Задание 16.9.3

class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.surname} {self.name}. {self.city}. Баланс: {self.balance} руб."'

client_1 = Clients('Петров', 'Иван', 'Москва', '1500')
print(client_1)

print("-----------")

#Задание 16.9.4

class Clients_1:
    def __init__(self, name1, surname1, city1, balance1):
        self.name1 = name1
        self.surname1 = surname1
        self.city1 = city1
        self.balance1 = balance1

    def guests(self):
        return f'"{self.surname1} {self.name1}. {self.city1}"'

client_1 = Clients_1('Петров', 'Иван', 'Москва', '1500')
client_2 = Clients_1('Сидоров', 'Петр', 'Вологда', '0')
clients = [client_1, client_2]

print("Список гостей:")
for client in clients:
    print(client.guests())


