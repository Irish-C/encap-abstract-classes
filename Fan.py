class Fan:
    # constant for fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    """ constructor for the four data field """
    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color


    """ Accesor(Getter) and Mutator (Setter) methods """
    # a method that returns the current speed
    def get_speed(self):
        return self.__speed
    
    # a method that sets the new speed
    def set_speed(self, speed):
        self.__speed = speed

    # a method that returns False when Fan is off
    def turn_on(self):
        return self.__on

    # a method that returns False when Fan is on
    def turn_on(self, on):
        self.__on = True

    # a method that returns the current radius
    def get_radius(self):
        return self.__radius

    # a method that sets the new radius
    def set_radius(self, radius):
        self.__radius = radius

    # a method that returns the current color 
    def get_color(self):
        return self.__color

    # a method that sets the new color
    def set_color(self, color):
        self.__color = color