# Домашнее задание по теме "Режимы открытия файлов"

# Задача "Учёт товаров":

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f"{self.name}, {self.weight}, {self.category}")

class Shop:
    __file_name = 'products.txt'

    def check_list(self, prod):
        if prod in self.get_products():
            return False
        else:
            return True

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for i in products:
            if i.__str__() in self.get_products():
                print(f"Продукт {i} уже есть в магазине")
                continue
            else:
                file.write(f"{i.__str__()}\n")
        file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        str = file.read()
        file.close()
        return str


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

print(s1.get_products())

s1.add(p1, p2, p3)

