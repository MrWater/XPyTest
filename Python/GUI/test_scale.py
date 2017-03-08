import tkinter


root = tkinter.Tk()

# 默认最大值100 最小值0 步距1
tkinter.Scale(root).pack()
# from_而不是from
# resolution步距
# digits 控制显示位数
v = tkinter.StringVar()
scale = tkinter.Scale(root, label='choice:', from_=-500, digits=8, variable=v, to=500, resolution=5, orient=tkinter.HORIZONTAL, command=lambda text: print(text + ' ' + v.get()))
scale.pack()
scale.set(12)
print(scale.get())

root.mainloop()