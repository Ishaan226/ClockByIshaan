from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font= ("font name", 90), background="black", foreground="colour")
label.pack(anchor="center")
time()

mainloop()

PS: For 12 hour format you can use %I:%M:%S %p and for 24 Hour format %H:%M:%S %p
