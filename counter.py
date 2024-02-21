from tkinter import *
from tkinter import font

root = Tk()
root.title("Counter")
root.geometry("640x400")

count = 0

lbl_font = font.Font(family="Verdana", weight="normal", size=150)
lbl_counter = Label(root, text=str(count), font=lbl_font)
lbl_counter.pack(side='top', fill='x')


def increase_lbl():
    global count
    count += 1

    lbl_counter.config(text=str(count))


btn_font = font.Font(family='Verdana', weight='normal', size=20)
btn_inc = Button(root)
btn_inc.config(text="+", font=btn_font)
btn_inc.config(height=5)
btn_inc.pack(side='left', expand=True, fill='both')
btn_inc.config(command=increase_lbl)


def reset_lbl():
    global count
    count = 0
    lbl_counter.config(text=str(count))


btn_reset = Button(root)
btn_reset.config(text='0', font=btn_font)
btn_reset.config(height=5)
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
