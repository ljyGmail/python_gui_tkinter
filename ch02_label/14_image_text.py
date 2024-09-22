from tkinter import *

root = Tk()
root.title("Image Text")
sse_text = """SSE全名是Silicon Stone Education，这家公司在美国，
这是国际专业证照公司，产品多元与丰富."""
image = PhotoImage(file="ch01_basics/images/mygithub.png")
# image = PhotoImage(file="ch02_label/images/notebook.jpg")
# label = Label(root, text=sse_text, image=image, bg="blue", compound="left")
# label = Label(
#     root, text=sse_text, image=image, bg="blue", justify="left", compound="right"
# )
label = Label(root, text=sse_text, image=image, bg="blue", compound="center")
label.pack()

root.mainloop()
