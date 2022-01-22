from tkinter import *
import datetime

root = Tk()

lab = Label(root)
lab.pack()
time = 0

def clock():
    global time
    time = str(int(time)+1)
    lab.config(text=time)
    #lab['text'] = time
    root.after(1000, clock) # run itself again after 1000 ms
    
# run first time
clock()

root.mainloop()