# import Car module
from Car import Car
import tkinter as tk
from tkinter import ttk
import time


""" Create methods for Test Program """

# a method that returns a current speed
def update_car_speed():
    current_speed = car1.get_speed()
    speed_label.config(text=f"Current Speed: {current_speed} mph")

# a method that updates loading bar
def update_loading_bar(value):
    global loading_bar
    loading_bar['value'] = value


""" Display Car object with tkinter as GUI """

# Create a car object
car1 = Car(2017, 'Volkswagen', '')

root = tk.Tk()
root.title('Car Testing')

car_info_label = tk.LabelFrame(root, text=f"Car: {car1._Car__year_model}, {car1._Car__make}")
car_info_label.pack()

# create a label for current speed
speed_label = tk.Label(root, text="Current Speed: 0 mph")
speed_label.pack()

# create a loading bar layout
loading_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
loading_bar.pack()

# Iterate acceleration five(5) times
def car1_acceleration():
    for i in range(5):
        car1.accelerate()
        update_car_speed()
        update_loading_bar((i+1) * 20)
        root.update()
        time.sleep(1)

    # Create label each acceleration
    car_speed_label = tk.Label(root, text=f"\nYour current Speed after 5x acceleration:  {car1.get_speed()} mph")
    car_speed_label.pack()

# Iterate deceleration five(5) times
def car1_brake():
    for i in range(5):
        car1.brake()
        update_car_speed()
        update_loading_bar((i+1) * 20)
        root.update()
        time.sleep(1)

    # Create label each deceleration
    car_speed_label = tk.Label(root, text=f"\nYour current Speed after 5x brake:  {car1.get_speed()} mph")
    car_speed_label.pack()


car1_acceleration()
car1_brake()
root.mainloop()