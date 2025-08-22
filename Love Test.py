#Importing different modules
import tkinter as tk
import random

#Creating the window
window = tk.Tk()
window.title("Love test")

#Defined function used for command
def click():
    #Validation of the given data through statements
    if name1.get() == "" and name2.get() == "":
        result.config(text = ("Both fields are empty, please fill them both in."))

    elif (name1.get() != "" and name2.get() == "") or (name1.get() == "" and name2.get() != ""):
        result.config(text = ("Only 1 field are empty, please fill them both in."))
    
    elif name1.get() == name2.get():
        result.config(text = ("Both names are the same, please change one of them or put in different names"))
    
    else:
        #Calculations are done here
        percentage = str(round(random.random() * 100))
        result.config(text = ("The result is" + " " + percentage + "%")) #Result is displayed

#Frames, Labels and Buttons are created here
frame = tk.Frame(window, background = "black")
first_name = tk.Label(frame, text = "Enter Name: ", background = "blue", foreground = "lime", font = ("Arial", 10, "bold"))
second_name = tk.Label(frame, text = "Enter Name: ", background = "red", foreground = "yellow", font = ("Arial", 10, "bold"))
name1 = tk.Entry(frame, width = 30)
name2 = tk.Entry(frame, width = 30)
button = tk.Button(frame, width = 10, text = "test", command = click)
result = tk.Label(frame, text = "Please enter the names", font = ("Comic Sans Ms", 10, "bold"), background = "black", foreground = "white")

#Placing frames, labels and buttons
frame.grid(row = 0, column = 0)
first_name.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "n")
second_name.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "n")
name1.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
button.grid(row = 2, column = 1, padx = 5, pady = 5)
name2.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "e")
result.grid(row = 3, column = 1, padx = 5, pady = 5)
window.mainloop()