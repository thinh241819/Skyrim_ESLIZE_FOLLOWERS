from tkinter import *
from convertESL import convert_esl
root = Tk()
root.title("ESLIZE YOUR FOLLOWERS")

form = []
i = 1

# Define class entry box
class EntryBox:
    def __init__(self):
        self.entry_formID = Entry(root, width=50, borderwidth=5)
        self.entry_path = Entry(root, width=50, borderwidth=5)
    def put_on_screen(self, index):
        self.entry_formID.grid(row=index, column=0)
        self.entry_formID.insert(0, "Enter your new form-ID")
        self.entry_path.grid(row=index, column=1)
        self.entry_path.insert(0, "Enter your follower's folder path")

# Entry boxes
box1 = EntryBox()
box1.put_on_screen(0)
form.append(box1)

# add entry boxes functions
def add_box():
    global i
    newBox = EntryBox()
    newBox.put_on_screen(i)
    i += 1
    form.append(newBox)

def execute_program():
    for items in form:
        convert_esl(items.entry_formID.get(), items.entry_path.get())

# Button to execute the programm
button_execute_eslize = Button(root, text="Eslize the follower", padx=20, pady=20, command=execute_program)
button_execute_eslize.grid(row=0, column=2)

button_new = Button(root, text="Create new box", padx=20, pady=20, command=add_box)
button_new.grid(row=1, column=2)

root.mainloop()
