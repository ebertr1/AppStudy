from controls.tda.stack.stackOperation import StackOperation

class StackArray ():
    def __init__(self, tope):
        self.__stack = StackOperation(tope)
    
    def push(self, data):
        self.__stack.push(data)
    
    def pop(self):
        return self.__stack.pop
    
    def verify(self):
        return self.__stack.verifyTope
    
    def print(self):
        self.__stack.print
    