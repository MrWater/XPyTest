import tkinter


root = tkinter.Tk()

# 不指定绑定变量，每个raiobutton自成一组
tkinter.Radiobutton(root, text='python').pack()
tkinter.Radiobutton(root, text='tkinter').pack()

v = tkinter.IntVar()
v.set(1)

# variable绑定到同一个变量，并且要设置value为1即选中的button
# 若value设置为相同，则工作方式一致，选中一个其他也会被选中
for i in range(3):
	tkinter.Radiobutton(root, variable=v, text=i, value=i, command=lambda: print(i)).pack()

# indicatoron 缺省值为1,
tkinter.Radiobutton(root, indicatoron=0, text='indicatoron').pack()
root.mainloop()