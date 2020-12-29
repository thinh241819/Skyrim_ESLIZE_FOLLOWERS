from tkinter import *
from convertESL import convert_esl
root = Tk()
root.title("ESLIZE YOUR FOLLOWERS")

# Entry boxes
entry_new_form_ID = Entry(root, width=50, borderwidth=5)
entry_new_form_ID.grid(row=0, column=0)
entry_new_form_ID.insert(0, "Enter your new form-ID")
entry_follower_folder_path = Entry(root, width=50, borderwidth=5)
entry_follower_folder_path.grid(row=0, column=1)
entry_follower_folder_path.insert(0, "Enter your follower's folder path")

# Button to execute the programm
button_execute_eslize = Button(root, text="Eslize the follower", padx=20, pady=20, command=lambda: convert_esl(entry_new_form_ID.get(), entry_follower_folder_path.get()))
button_execute_eslize.grid(row=1, column=0)

root.mainloop()
