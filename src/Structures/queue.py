from Structures.nodeDePila import Node

class Queue:
    def __init__(self):
        self.front = None
        self.last = None
        self.size = 0
    
    def enqueue(self, data):
        if data is None:
            raise ValueError("- QueueError: El dato es nulo, no pudo ser agregado a la cola")
        
        new_node = Node(data=data)
        
        if self.is_empty():
            self.front = new_node
        else:
            self.last.set_next(new_node)
        self.last = new_node
        
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError("- QueueError: la cola esta vacia")
        
        data = self.front.get_data()
        self.front = self.front.get_next()
        
        if self.front is None:
            self.last = None
        
        self.size -= 1
        return data
    
    def get_peek(self):
        if self.is_empty():
            raise ValueError("- QueueError: la cola esta vacia")
        return self.front.get_data()
    
    def get_size(self):
        return self.size
    
    def show_last(self):
        print(self.last)
    
    def is_empty(self):
        return self.front is None and self.size == 0 # type: ignore