from tkinter import *

root = Tk()
screenWidth = root.winfo_screenwidth()  # 屏幕宽度
screenHeight = root.winfo_screenheight()  # 屏幕高度
w = 300
h = 160
x = (screenWidth - w) / 2
y = (screenHeight - h) / 2
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
root.mainloop()
