# import necessary modules
from Pet import Pet
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import time

# Create TestPet class
class TestPet:
    def __init__(self):
        self.pet = Pet()

        # Create TestPet window
        self.root = tk.Tk()
        self.root.title('My Pet Profile')
        self.root.geometry('300x250')

        # An input feature for the pet's name
        self.pet_label = ttk.Label(self.root, text="Pet Name:")
        self.pet_label.pack()
        self.pet_entry = ttk.Entry(self.root)
        self.pet_entry.pack()