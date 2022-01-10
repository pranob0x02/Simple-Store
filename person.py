class person:
    def __init__(self, name, id, phoneNumber):
        self.__name = name
        self.__id = id
        self.__phoneNumber = phoneNumber

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getPhoneNumber(self):
        return self.__phoneNumber

    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def printInfo(self):
        print(f"Name: {self.__name}")
        print(f"Identification Number: {self.__id}")
        print(f"Phone Number: {self.__phoneNumber}")
