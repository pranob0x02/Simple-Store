from person import person


class employee(person):
    def __init__(self, name, id, phoneNumber, salary, employeeId, position):
        super().__init__(name, id, phoneNumber)
        self.__salary = salary
        self.__employeeId = employeeId
        self.__position = position

    def getSalary(self):
        return self.__salary

    def setSalary(self, salary):
        self.__salary = salary

    def getEmployeeId(self):
        return self.__employeeId

    def setEmployeeId(self, employeeId):
        self.__employeeId = employeeId

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position

    def printInfo(self):
        super().printInfo()
        print(f"Salary: {self.__salary}")
        print(f"Employee ID: {self.__employeeId}")
        print(f"Job description: {self.__position}")
