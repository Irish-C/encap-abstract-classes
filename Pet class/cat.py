import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Pet information
name = "Fluffy"
animal_type = "Cat"
age = 5
age_unit = "years"

# A frame to hold the pet information
pet_info_frame = ttk.LabelFrame(root, text="PET INFORMATION", width=30, height=300)
pet_info_frame.pack(side=tk.LEFT, padx=10, pady=10)

# A label to display the pet's information
pet_info_label = ttk.Label(pet_info_frame, text=f'''                   
                ╱|、    Pet Name: {name}
            !! (˚, 。7  Animal Type: {animal_type}
                |、˜〵  Age: {age} {age_unit}      
                じしˍ,)ノ 𓆝 𓆟 𓆞 𓆝 𓆟
                \n''', font=("Arial", 12))  # Adjust the font as needed
pet_info_label.pack()

# Change the font of the pet_info_label
pet_info_label.config(font=("Courier", 10))  # Adjust the font as needed

root.mainloop()
