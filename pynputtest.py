from pynputtemplate import on_press
from pynput import keyboard
from tkintertemplate import *

with keyboard.Listener(
        on_press=on_press,) as listener:
    x=listener.join()
x=0
testing = tk.Label(
    text=x,
)

testing.pack()
window.mainloop