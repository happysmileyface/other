import win32gui as win32
from tkintertemplate import *
from pynputtemplate import on_press,on_release
from tkinter import messagebox

window.title("Input Display")
current_window = (win32.GetWindowText(win32.GetForegroundWindow()))
desired_window = "Input Display"
global x
x = "0"
y="0"
def on_closing():
     if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy() 
def exit_window():
    on_closing()
def tell_inputs():
    global y
    y = str(int(y)+1)
    tell_button_presses.config(text = y)
def keep_updating():
    window.mainloop()
    window.after(1,keep_updating)

tell_button_presses = tk.Label(
text=x,
font=(25),
)
close_button = tk.Button(
    text="Close",
    command=exit_window,
    width=20,
    height=4,
)

close_button.pack()
tell_button_presses.pack()
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()