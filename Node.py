class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def setData(self, data):
        self.__data = data

    def setNext(self, nextNode):
        self.__next = nextNode

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def __str__(self):
        return f"{self.__data} -> {self.__next}"