from tkinter import *

root = Tk()
root.title("Label")
# label = Label(root, text="I like tkinter")
# label.pack() # 包装与定位组件
# label = Label(root, text="I like tkinter").pack()
# print(type(label))  # 传回Label数据类型

Label(root, text="I like tkinter").pack()

root.mainloop()
