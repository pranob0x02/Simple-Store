class item():
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def productDetails(self):
        return f"Name: {self.__name} \nPrice: {self.__price}"


Mango = item("Mango", 10)
# print(Mango.productDetails())
Apple = item("Apple", 2)
Orange = item("Orange", 5)
