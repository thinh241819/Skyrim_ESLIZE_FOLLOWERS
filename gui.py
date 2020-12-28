from tkinter import *
from convertESL import convert_esl
root = Tk()

# Entry boxes
entry_new_form_ID = Entry(root, width=50)
entry_new_form_ID.pack()
entry_new_form_ID.insert(0, "Enter your new form-ID")
entry_follower_folder_path = Entry(root, width=50)
entry_follower_folder_path.pack()
entry_follower_folder_path.insert(0, "Enter your follower's folder path")

# Button to execute the programm
button_execute_eslize = Button(root, text="Eslize the follower", command=lambda: convert_esl(entry_new_form_ID.get(), entry_follower_folder_path.get()))
button_execute_eslize.pack()

root.mainloop()
