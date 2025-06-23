class SystemDontHaveSolution(Exception):
    def __init__(self, message:str):
        super().__init__(message)

class NumberIsInvalid(Exception):
    def __init__(self, message:str):
        super().__init__(message)
    
class NoneType(Exception):
    def __init__(self, message:str):
        super().__init__(message)

