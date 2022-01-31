import keyboard
from tkintertemplate import *

x="|"
y="0"
def count():
    global y
    y=str(int(y)+1)
    countdown.config(text=y)
    window.after(1000,count)
def ask():
    global x
    while True:
        if keyboard.is_pressed('q'):
            x="q "+x
            display.config(display(text=x))
        if keyboard.is_pressed("esc"):
            window.destroy()
display = tk.Label(
    text=x
)
countdown = tk.Label(
    text=y
)
countdown.pack()
display.pack()
count()
window.mainloop()
ask()


