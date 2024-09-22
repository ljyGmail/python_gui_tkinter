from tkinter import *

root = Tk()
root.title("Compound")
# label=Label(root,bitmap="hourglass",compound="left",text="我的天空")
# label=Label(root,bitmap="hourglass",compound="top",text="我的天空")
label = Label(root, bitmap="hourglass", compound="center", text="我的天空")
label.pack()

root.mainloop()
