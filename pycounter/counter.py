from tkinter import *
from tkinter import font
from tkinter import ttk


root = Tk()
root.title("Counter")
root.geometry("640x400")

style = ttk.Style()
style.configure("TLabel", font=('Verdana', 150), foreground="red")
style.configure("Inc.TButton", font=('Verdana', 30), foreground="blue")
style.configure("Rst.TButton", font=('Verdana', 30), foreground="black")

count = 0

lbl_counter = ttk.Label(root, text=str(count))
lbl_counter.configure(style='TLabel')
lbl_counter.configure(anchor="center")
lbl_counter.pack(side='top', fill='x')


def increase_lbl():
    global count
    count += 1

    lbl_counter.config(text=str(count))


btn_inc = ttk.Button(root)
btn_inc.config(text='+')
btn_inc.config(style='Inc.TButton')
btn_inc.pack(side='left', expand=True, fill='both')
#btn_inc.pack(side='left', fill='both', anchor='w')

btn_inc.config(command=increase_lbl)


def reset_lbl():
    global count
    count = 0
    lbl_counter.config(text=str(count))


btn_reset = ttk.Button(root)
btn_reset.config(text='0')
btn_reset.configure(style='Rst.TButton')
btn_reset.pack(side='right', expand=True, fill='both')

btn_reset.config(command=reset_lbl)


def decrease_lbl():
    global count
    if count > 0:
        count -= 1
        lbl_counter.config(text=str(count))


def key_handler(event):
    if event.keycode == 27:     # esc
        reset_lbl()
    elif event.keycode == 8:    # backspace
        decrease_lbl()
    else:
        increase_lbl()


root.bind('<Key>', key_handler)

root.mainloop()
