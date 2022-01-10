from item import item


class basket():
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def totalNumberOfItems(self):
        return len(self.items)

    def totalPrice(self):
        total = 0
        for i in self.items:
            total = total + i.getPrice()
        return total


Mango = item("Mango", 10)
# print(Mango.productDetails())
Apple = item("Apple", 2)
Orange = item("Orange", 5)

b1 = basket()

b1.addItem(Mango)
b1.addItem(Orange)

print(b1.totalNumberOfItems())
print(b1.totalPrice())
