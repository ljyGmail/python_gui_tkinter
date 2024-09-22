from tkinter import *

root = Tk()
root.title("Cursor")
label = Label(
    root,
    text="raised",
    relief="raised",
    bg="lightyellow",
    padx=5,
    pady=10,
    cursor="heart",
)  # 光标形状
label.pack()

root.mainloop()
