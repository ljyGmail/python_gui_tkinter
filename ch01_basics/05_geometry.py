from tkinter import *

root = Tk()
# root.geometry("300x160+400+200") # 距离屏幕左上角(400, 200)

# 另一种方式
w = 300
h = 160
x = 400
y = 200

root.geometry("%dx%d+%d+%d" % (w, h, x, y))

root.mainloop()
