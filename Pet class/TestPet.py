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

        # Create window
        self.root = tk.Tk()
        self.root.title('My Pet Profile')
        self.root.geometry('300x250')