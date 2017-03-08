import tkinter


root = tkinter.Tk()

# 想要不换行，设置足够宽的宽度
tkinter.Message(root, text='message', width=60).pack()


root.mainloop()