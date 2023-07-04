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