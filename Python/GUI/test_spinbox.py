import tkinter


root = tkinter.Tk()

# 设置最大最小值，步距值
# textvariable绑定变量
# command
tkinter.Spinbox(root, from_=0, to=100, increment=5).pack()

spinbox = tkinter.Spinbox(root, values=(0,2,20,40,-1), increment=12, command=lambda: print(1))
spinbox.pack()
spinbox.delete(0)

root.mainloop()