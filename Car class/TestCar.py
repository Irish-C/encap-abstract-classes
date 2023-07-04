# import Car module
from Car import Car
import tkinter as tk
import time

# Create TestCar class
class TestCar:

    # a method that returns a current speed
    def update_car_speed(self):
        current_speed = car1.get_speed()
        current_speed.config(text=f"Current Speed: {current_speed} mph")

# Create a car object
car1 = Car(2017, 'Volkswagen')