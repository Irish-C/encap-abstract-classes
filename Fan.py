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