class Person:
    def __init__(self, name, age, id):
        self.__name = name
        self.__age = age
        self.__id = id
        
    def get_info(self):
        return self.__name, self.__age
        
    def get_older(self):
        self.__age += 1
        
    def get_id(self):
        return self.__id