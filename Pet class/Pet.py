# Pet class
class Pet:
    # constructor
    def __init__(self, name, animal_type, age):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    # a method that sets the pet's name
    def set_name(self, name):
        self.__name = name

    # a method that sets what type of animal
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # a method that sets the pet's age
    def set_age(self, age):
        self.__age = age

    # a method that returns the pet's name
    def get_name(self):
        return self.__name

    # a method that returns what type of animal
    def get_animal_type(self):
        return self.__animal_type

    # a method that returns the pet's age
    def get_age(self):
        return self.__age