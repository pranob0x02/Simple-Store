from employee import employee


class manager(employee):
    def __init__(self, name, id, phoneNumber, salary, employeeId, position, password):
        super().__init__(name, id, phoneNumber, salary, employeeId, position)
        self.__password = password

    def printInfo(self):
        super().printInfo()


Sanjoy = employee("Sanjoy", 390803300078, 54290842, 2000, 690, "Manager")

Sanjoy.printInfo()
