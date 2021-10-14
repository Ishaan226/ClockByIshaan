# ClockByIshaan

from tkinter import *
from tkinter import font
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%I:%H:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font= ("font name", 90), background="black", foreground="colour")
label.pack(anchor="center")
time()

mainloop()
