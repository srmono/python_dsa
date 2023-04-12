class College:
    def __init__(self):
        self.__name = ''
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @name.deleter
    def name(self):
        del self.__name
        
c = College()
c.name = "AS College"

print(c.name)
del c.name
print(c.name)