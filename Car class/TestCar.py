# import Car module
from Car import Car
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import time


""" Create methods for Test Program """

# a method that returns a current speed
def update_car_speed():
    current_speed = car1.get_speed()
    speed_label.config(text=f"{current_speed} mph")

# a method that updates loading bar
def update_loading_bar(value):
    global loading_bar
    loading_bar['value'] = value


""" Display Car object with tkinter as GUI """

# Create a car object
car1 = Car(2017, 'Volkswagen','')

# Name the window, and make window appear at the center
root = ThemedTk(theme="arc")
root.title('Car Testing')
root.eval('tk::PlaceWindow {} center'.format(root.winfo_toplevel()))

# Create Car info of car1 into a frame
car_info_frame = tk.LabelFrame(root, text="MY CAR")
car_info_frame.pack()
car_info_label = tk.Label(car_info_frame, text=f"\nYear: {car1._Car__year_model}\nMake: {car1._Car__make}\n", font=("Arial", 11))
car_info_label.pack()

# create a loading bar layout
loading_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
loading_bar.pack()

# create a label for current speed
speed_label = tk.Label(root, text="\n0 mph")
speed_label.pack()



# Iterate acceleration five(5) times
def car1_acceleration():
    for i in range(-1,5,1):
        time.sleep(1)
        car1.accelerate()
        update_car_speed()
        update_loading_bar((i+1) * 20)
        root.update()

    # Create label each acceleration
    car_speed_label_1 = tk.Label(root, text=f"\nMy current Speed: {car1.get_speed()} mph", font=("Arial", 12))
    car_speed_label_1.pack()
    car_speed_label_2 = tk.Label(root, text="After 5x acceleration")
    car_speed_label_2.pack()

# Iterate deceleration five(5) times
def car1_brake():
    for i in range(5):
        car1.brake()
        update_car_speed()
        update_loading_bar((i+1) * 20)
        root.update()
        time.sleep(1)

    # Create label each deceleration
    car_speed_label = tk.Label(root, text=f"My current Speed:  {car1.get_speed()} mph", font=("Arial", 12))
    car_speed_label.pack()
    car_speed_label_2 = tk.Label(root, text="After 5x brake")
    car_speed_label_2.pack()


car1_acceleration()
car1_brake()
root.mainloop()