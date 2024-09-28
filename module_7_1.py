class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        s = file.read()
        file.close()
        return s

    def add(self, *products):
        file = open(self.__file_name, 'r')
        s = file.read()
        file.close()
        file = open(self.__file_name, 'a')
        for i in products:
            if i.name not in s:
                file.write(f'{i.name}, {i.weight}, {i.category}\n')
            else:
                print(f'Продукт {i.name} есть в магазине!')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

#
# name = 'sample.txt'
# file = open(name, 'r')
# print(file)
# print(file.read(), '\n')
# print(file.tell())
# file.seek(5)
# print(file.read())
# file.close()
# #
# name = 'sample2.txt'
# file = open(name, 'a')
# print(file)
# file.write('Hello, World!\n')
# file.close()