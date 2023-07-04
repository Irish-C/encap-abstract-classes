# import necessary modules
from Pet import Pet
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import time

# Create TestPet class
class TestPet():
    def __init__(self):
        self.pet = Pet("", "", 0)

        # Create TestPet window
        self.root = tk.Tk()
        self.root.title('My Pet Profile')
        self.root.geometry('300x250')

        # An input feature for the pet's name
        self.name_label = ttk.Label(self.root, text="Pet Name:")
        self.name_label.pack()
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.pack()

        # An input feature for the pet's animal type
        self.type_label = ttk.Label(self.root, text="Animal Type:")
        self.type_label.pack()
        self.type_entry = ttk.Entry(self.root)
        self.type_entry.pack()

        # An input feature for the pet's age
        self.age_label = ttk.Label(self.root, text="Age:")
        self.age_label.pack()
        self.age_entry = ttk.Entry(self.root)
        self.age_entry.pack()

if __name__ == "__main__":
    gui = TestPet()
    gui.root.mainloop()