import win32gui as win32
from tkintertemplate import *
import keyboard
from tkinter import messagebox

window.title("Input Display")
current_window = (win32.GetWindowText(win32.GetForegroundWindow()))
desired_window = "Input Display"
def on_closing():
     if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy() 
def exit_window():
    window.destroy()
def tell_inputs():
    global x
    x= keyboard.read_key() + " -- " + x
    tell_button_presses.configure(text=x)
global x
x = "(button)"
tell_button_presses = tk.Label(
text="[Button]",
font=(25),
)
close_window = tk.Button(
    text="Close",
    command=exit_window,
    width=20,
    height=4,
) 
close_window.pack()
tell_button_presses.pack()
if __name__ == "__main__" and current_window == desired_window:
    if keyboard.is_pressed("r"):
        tell_inputs()
window.mainloop()
