class Fan:
    # constant for fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # constructor
    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # Accesor methods (Getter)
    def get_speed(self):
        return self.__speed
    
    def get_on(self):
        return self.__on
    
    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color