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
        self.animal_type_label = ttk.Label(self.root, text="Animal Type:")
        self.animal_type_label.pack()
        self.animal_type_entry = ttk.Entry(self.root)
        self.animal_type_entry.pack()

        # An input feature for the pet's age
        self.age_label = ttk.Label(self.root, text="Age:")
        self.age_label.pack()
        self.age_entry = ttk.Entry(self.root)
        self.age_entry.pack()

        # a save button for pet profile
        self.save_button = ttk.Button(self.root, text="Save", command=self.save_pet)
        self.save_button.pack()

    # a method that gets the name, animal_type, and age of the pet
    def save_info(self):
        name = self.name_entry.get()
        animal_type = self.animal_type_entry.get()
        age = self.age_entry.get()
    
        if age.isdigit():  # Check if age is a positive integer value
            self.pet.set_name(name)
            self.pet.set_animal_type(animal_type)
            self.pet.set_age(int(age))



if __name__ == 'main':
    test_pet = TestPet()
    test_pet.root.mainloop()