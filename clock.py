from tkinter import *
from time import strftime

theWindow = Tk()
theWindow.title("Clock")
theWindow.resizable(False, False)

def time():
    theTime = strftime('%H:%M:%S %p')
    clock.config(text=theTime)
    clock.after(1000, time)

clock = Label(theWindow, font= ('arial', 40, 'bold'), background = "#000000", foreground = 'red', )
clock.pack(anchor = 'center')
time()
mainloop()