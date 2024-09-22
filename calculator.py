from tkinter import *
import tkinter

# Create the main window
root = tkinter()
root.title("Calculator")
root.geometry("400x600")  # Set window size
root.configure(bg="#F0F0F0")  # Set background color

# Create entry field for user input
entry_field = Entry(root, width=16, borderwidth=5, font=('Arial', 24), bg="#FFFFFF")
entry_field.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# Function to update the entry field
def update_entry_field(value):
    current = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(current) + str(value))

# Function to clear the entry field
def clear_entry_field():
    entry_field.delete(0, END)

# Function to calculate the result
def perform_calculation():
    try:
        calculation = entry_field.get()
        result = eval(calculation)
        entry_field.delete(0, END)
        entry_field.insert(0, result)
    except Exception:
        entry_field.delete(0, END)
        entry_field.insert(0, "Error")

# Define button design
button_style = {
    'padx': 30,
    'pady': 20,
    'font': ('Arial', 18),
    'bg': '#E0E0E0',
    'activebackground': '#C0C0C0',
}

# Creating number buttons
buttons = []
for i in range(10):
    buttons.append(Button(root, text=str(i), command=lambda x=i: update_entry_field(x), **button_style))

# Creating operator buttons
button_add = Button(root, text="+", command=lambda: update_entry_field("+"), **button_style)
button_subtract = Button(root, text="-", command=lambda: update_entry_field("-"), **button_style)
button_multiply = Button(root, text="*", command=lambda: update_entry_field("*"), **button_style)
button_divide = Button(root, text="/", command=lambda: update_entry_field("/"), **button_style)
button_equals = Button(root, text="=", command=perform_calculation, padx=90, **button_style)
button_clear = Button(root, text="Clear", command=clear_entry_field, padx=70, **button_style)

# Placing number buttons on the grid
for i in range(1, 10):
    buttons[i].grid(row=(i-1)//3 + 1, column=(i-1)%3)

buttons[0].grid(row=4, column=1)

# Placing operator buttons on the grid
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equals.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=0, column=3)

# Start the main loop
root.mainloop()

