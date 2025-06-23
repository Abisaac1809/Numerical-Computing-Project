class Node:
    def __init__(self, data=None, copy=None):
        if copy is not None:
            if copy is None:
                raise ValueError("- RefError: Copia fallida por nodo nulo")
            self.data = copy.get_data()
            self.next = copy.get_next()
        elif data is not None:
            if data is None:
                raise ValueError("- RefError: Data no puede ser None")
            self.data = data
            self.next = None
        else:
            self.data = None
            self.next = None
    
    def set_data(self, data):
        if data == self.data:
            raise ValueError("- RefError: Tiene el mismo dato")
        if data is None:
            raise ValueError("- RefError: El dato es nulo")
        self.data = data
    
    def set_next(self, next_node):
        self.next = next_node
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def is_equals(self, obj):
        if self == obj:
            return True
        if obj is None or not isinstance(obj, Node):
            return False
        return self.data == obj.data
    
    def __str__(self):
        return f"{{Valor = {self.data}}}"