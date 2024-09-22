from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title("Separator")

myTitle = "一个人的极境旅行"
myContent = """2016年12月，我一个人订了机票和船票，
开始我的南极旅行，飞机经迪拜再往阿根廷的乌斯怀亚，
在此我登上邮轮开始我的南极之旅"""

lab1 = Label(root, text=myTitle, font="Helvetic 20 bold")
lab1.pack(padx=10, pady=10)

sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=5)

lab2 = Label(root, text=myContent)
lab2.pack(padx=10, pady=10)

root.mainloop()
