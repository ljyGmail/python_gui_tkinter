from tkinter import *

root = Tk()
root.title("Keys")
label = Label(root, text="I like tkinter")
label.pack()
print(label.keys())

root.mainloop()
