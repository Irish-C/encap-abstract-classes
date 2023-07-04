class Car:
    # constructor
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0


    # a method that add 5 each time its called
    def accelerate(self):
        self.__speed += 5

    # a method that subtract 5 each time its called
    def brake(self):
        self.__speed -= 5
    
    # a method that returns the current speed
    def get_speed(self):
        return self.__speed