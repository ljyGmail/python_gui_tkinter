from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Show JPG")
root.geometry("680x400")

image = Image.open("ch02_label/images/notebook.jpg")
notebook = ImageTk.PhotoImage(image)
label = Label(root, image=notebook)
label.pack()

root.mainloop()
