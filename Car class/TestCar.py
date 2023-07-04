# import Car module
from Car import Car
import tkinter as tk
from tkinter import ttk

# a method that returns a current speed
def update_car_speed():
    current_speed = car1.get_speed()
    current_speed.config(text=f"Current Speed: {current_speed} mph")

# a method that updates loading bar
def update_loading_bar(value):
    global loading_bar
    loading_bar['value'] = value


# Create a car object
car1 = Car(2017, 'Volkswagen', '')

root = tk.Tk()
root.title('Car Testing')

speed_label = tk.Label(root, text="Current Speed: 0 mph")
speed_label.pack()

loading_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
loading_bar.pack()

root.mainloop()