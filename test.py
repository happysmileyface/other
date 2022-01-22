import keyboard
from pip import main
from tkintertemplate import *
from tkinter import mainloop, messagebox
import time
countdown = "0"
def on_closing():
     if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy() 
def countdown_timer():
    global countdown
    countdown = str(int(countdown)+1)
    countdown_display.config(text = countdown)
    window.after(1000,countdown_timer)
    
countdown_display = tk.Label(
    text = countdown
)
countdown_display.pack()
window.protocol("WM_DELETE_WINDOW", on_closing)
countdown_timer()
window.mainloop()