from tkinter import *
from tkinter import ttk
import translator
root = Tk()
root.geometry("500x500")
root.title("LANGUAGE TRANSLATOR")
root.config(background = "#F2CCC3")

label = Label(root, text = "LANGUAGE TRANSLATOR", bg = "red", font = ("Arial Unicode MS", 15, "bold"))
label.place(relx = 0.02, rely = 0.2, anchor = W)

input_label = Label(root, text = "Enter Text:- ", bg = "blue", font = ("Arial Unicode MS", 10, "bold"))
input_label.place(relx = 0.02, rely = 0.3, anchor = W)

input_text = Text(root, bg = "white", font = ("Arial Unicode MS", 10, "bold"), height = 20, width = 30, padx = 10, pady = 10, border = bd)
input_text.place(relx = 0.02, rely = 0.5, anchor = CENTER)
root.mainloop()