from Node import Node

class MyQueue:
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head is None

    def push(self, e):
        newNode = Node(e)
        if self.isEmpty():
            self.__head = newNode
        else:
            aux = self.__head
            while aux.getNext() is not None:
                aux = aux.getNext()
            aux.setNext(newNode)

    def poll(self):
        if self.isEmpty():
            return None
        else:
            rta = self.__head.getData()
            self.__head = self.__head.getNext()
            return rta

    def peek(self):
        return self.__head.getData()

    def showContent(self):
        return self.__head.__str__()
