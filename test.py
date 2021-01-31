from tkinter import *
from tkinter.scrolledtext import ScrolledText
root = Tk()

box = ScrolledText(root, width=15)
box.pack()

for i in range(20):
    frame = Frame()
    label = Label(frame, text=f"item {i}")
    label.pack(side=LEFT)
    button = Button(frame, text="click")
    button.pack(side=LEFT)
    box.window_create(END, window=frame)
    box.insert(END, '\n')

root.mainloop()