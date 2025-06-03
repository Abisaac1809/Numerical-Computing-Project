from Structures.Node import Node

class ListaDoble:
    def __init__(self):
        self.__head:Node = None
        self.__tail:Node = None
        self.__size = 0
    
    def isEmpty(self) -> bool:
        return self.__size == 0
    
    def get_size(self) -> int:
        return self.__size
    
    def get(self, index:int) -> any:
        if (index < 0 or index >= self.__size):
            raise IndexError("Error: El índice es inválido")
        
        current:Node = self.__head
        for i in range(index):
            current = current.getNext()
        return current.getData()
        
        
    
    def addLast(self, data:any) -> None:
        nuevo_nodo:Node = Node(data)
        
        if self.isEmpty():
            self.__head = nuevo_nodo
            self.__tail = nuevo_nodo
        else:
            nuevo_nodo.set_prev(self.__tail)
            self.__tail.set_next(nuevo_nodo)
            self.__tail = nuevo_nodo
        
        self.__size += 1
    
    def addFirst(self, data:any) -> None:
        nuevo_nodo = Node(data)
        
        if self.isEmpty():
            self.__head = nuevo_nodo
            self.__tail = nuevo_nodo
        else:
            nuevo_nodo.set_next(self.__head)
            self.__head.set_prev(nuevo_nodo)
            self.__head = nuevo_nodo
            
        self.__size += 1
    
    def removeLast(self) -> None:
        if self.isEmpty():
            raise Exception("La lista está vacía")
        
        data = self.__tail.get_data()
        
        if self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.get_prev()
            self.__tail.set_next(None)
        
        self.__size -= 1
        return data
    
    def printList(self) -> None:
        actual = self.__head
        while actual:
            print(actual.get_data(), end=" <-> ")
            actual = actual.get_next()
        print("None")