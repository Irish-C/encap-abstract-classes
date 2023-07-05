# import necessary modules
from Pet import Pet
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create TestPet class
class TestPet:
    def __init__(self):
        self.pet = Pet("", "", 0)

        # Create TestPet window
        self.root = tk.Tk()
        self.root.title('My Pet Profile')
        self.root.geometry("600x400+{}+{}".format(int(self.root.winfo_screenwidth() / 2 - 300), 0))


        # A frame to hold the pet information
        self.pet_info_frame = ttk.LabelFrame(self.root, text="PET INFORMATION")
        self.pet_info_frame.pack()
        # A label to display the pet's information
        self.pet_info_label = ttk.Label(self.pet_info_frame, text=f'''                   
                            ╱|、
                        ? (˚ˎ 。7  
                           |、˜〵          
                          じしˍ,)ノ
                           Meow!\n''')
        self.pet_info_label.pack()


        # An input feature for the pet's name
        self.name_label = ttk.Label(self.root, text="\nPet Name:")
        self.name_label.pack()
        self.name_entry = ttk.Entry(self.root, justify='center')
        self.name_entry.pack()

        # An input feature for the pet's animal type
        self.animal_type_label = ttk.Label(self.root, text="Animal Type:")
        self.animal_type_label.pack()
        self.animal_type_entry = ttk.Entry(self.root, justify='center')
        self.animal_type_entry.pack()

        # An input feature for the pet's age
        self.age_label = ttk.Label(self.root, text="Age:")
        self.age_label.pack()
        self.age_entry = ttk.Entry(self.root, justify='center')
        self.age_entry.pack()
        # A Menu feature for the pet's age unit
        self.age_unit = ttk.Combobox(values=["days", "weeks", "months", "years"], justify='center')
        self.age_unit.current(0)
        self.age_unit.pack()

        # Add space between age entry and save button
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(3, weight=1)

        # A save button for pet profile
        self.save_button = ttk.Button(self.root, text="Save", command=self.save_pet_info)
        self.save_button.pack(pady=10)

        # A label to display messages
        self.message_label = ttk.Label(self.root, text="")
        self.message_label.pack()

    # a method that saves the pet's information
    def save_pet_info(self):
        name = self.name_entry.get()
        animal_type = self.animal_type_entry.get()
        age = self.age_entry.get()

        # Check if inputs are valid
        if name != "" and animal_type != "":
            if age.isdigit():
                self.pet.set_name(name)
                self.pet.set_animal_type(animal_type)
                self.pet.set_age(int(age))
                self.message_label.config(text="Pet information saved!\n")
                self.show_pet_info()
                
            else:
                self.message_label.config(text="Remember age is just a number ^_^\n")
        else:
            self.message_label.config(text="Please fill in all fields.\n")
    
    # A method that displays the pet's information
    def show_pet_info(self):
        name = self.pet.get_name()
        animal_type = self.pet.get_animal_type()
        age = self.pet.get_age()
        age_unit = self.age_unit.get()
        pet_info = f"Pet Name: {name}\nAnimal Type: {animal_type}\nAge: {age} {age_unit}, "
        self.pet_info_label.config(text=pet_info)
        messagebox.showinfo("Pet Information", pet_info)

