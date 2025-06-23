from Structures.nodeDePila import Node

class Stack:
    def __init__(self):
        self.stack = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data=data)
        new_node.set_next(self.stack)
        self.stack = new_node
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise ValueError("- StackError: la pila esta vacia")
        data = self.stack.get_data()
        self.stack = self.stack.get_next()
        self.size -= 1
        return data
    
    def show_stack(self):
        if self.is_empty():
            raise ValueError("- StackError: la pila esta vacia")
        return self.stack.get_data()
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.stack is None and self.size == 0