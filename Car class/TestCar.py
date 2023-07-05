# import Car module
from Car import Car
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import time

# Create TestCar class
class TestCar():

    # constructor
    def __init__(self):
        # Name the window, and make window appear at the center
        self.root = ThemedTk(theme="arc")
        self.root.title('Car Testing')
        self.root.geometry("600x400+{}+{}".format(int(self.root.winfo_screenwidth() / 2 - 300), 0))

        # Create a car object
        self.car1 = Car(2017, 'Volkswagen', 0)

        # Create Car info of car1 into a frame
        self.car_info_frame = tk.LabelFrame(self.root, text="MY CAR")
        self.car_info_frame.pack()
        self.car_info_label = tk.Label(self.car_info_frame, text=f"\nYear: {self.car1._Car__year_model}\nMake: {self.car1._Car__make}\n", font=("Arial", 11))
        self.car_info_label.pack()

        # create a loading bar layout
        self.loading_bar = ttk.Progressbar(self.root, orient="horizontal", length=200, mode="determinate")
        self.loading_bar.pack()

        # create a label for current speed
        self.speed_label = tk.Label(self.root, text="\n0 mph")
        self.speed_label.pack()

    def run(self):
        self.car1_accelerate()
        self.car1_brake()
        self.root.mainloop()

    # Iterate acceleration five(5) times
    def car1_accelerate(self):
        for i in range(5):
            time.sleep(1)
            self.car1.accelerate()
            self.update_car_speed()
            self.update_loading_bar((i+1) * 20)
            self.root.update()

        car_speed_label_1 = tk.Label(self.root, text=f"\nMy current Speed:  {self.car1.get_speed()} mph", font=("Arial", 12))
        car_speed_label_1.pack()
        car_speed_label_1 = tk.Label(self.root, text="After 5x acceleration")
        car_speed_label_1.pack()

    # Iterate brake five(5) times
    def car1_brake(self):
        for i in range(5):
            time.sleep(1)
            self.car1.brake()
            self.update_car_speed()
            self.update_loading_bar((i+1) * 20)
            self.root.update()

        car_speed_label_2 = tk.Label(self.root, text=f"\nMy current Speed:  {self.car1.get_speed()} mph", font=("Arial", 12))
        car_speed_label_2.pack()
        car_speed_label_2 = tk.Label(self.root, text="After 5x brake")
        car_speed_label_2.pack()

    # a method that returns a current speed
    def update_car_speed(self):
        current_speed = self.car1.get_speed()
        self.speed_label.config(text=f"{current_speed} mph")

    # a method that updates loading bar
    def update_loading_bar(self, value):
        self.loading_bar['value'] = value

test_car = TestCar()
test_car.run()