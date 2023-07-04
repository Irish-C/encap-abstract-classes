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

# create a label for current speed
speed_label = tk.Label(root, text="Current Speed: 0 mph")
speed_label.pack()

# create a loading bar layout
loading_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
loading_bar.pack()

# Iterate acceleration five(5) times
for i in range(5):
    car1.accelerate()
    update_car_speed()
    update_loading_bar((i+1) * 20)

    # Create label each acceleration
    car_speed_label = tk.Label(root, text=f"Speed #{i+1}: {car1.get_speed} mph")
    car_speed_label.pack()

    root.update()
    time.sleep(1)

root.mainloop()