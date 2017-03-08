import tkinter


root = tkinter.Tk()

# selectmode: single multiple browse(移动鼠标进行选中，而不是单击选中) EXTENDED支持shift和ctrl

listbox = tkinter.Listbox(root, selectmode=tkinter.MULTIPLE)
listbox.pack()

for i in range(19):
	listbox.insert(tkinter.END, i)

listbox = tkinter.Listbox(root, selectmode=tkinter.BROWSE)
listbox.pack()

for i in range(19):
	listbox.insert(tkinter.END, i)

listbox = tkinter.Listbox(root, selectmode=tkinter.EXTENDED)
listbox.pack()

for i in range(19):
	listbox.insert(tkinter.END, i)

# selection_set 两个参数索引表示范围，一个则选中一个
# selection_clear 取消选中
# curselection() 当前选中项，而不是索引
# selection_includes(index) 判断某个索引是否被选中
# listvariable 绑定变量
# listbox不支持command设置毁掉函数，必须使用bind来指定
print(listbox.size())
print(listbox.get(3))
print(listbox.get(3,9))
listbox.bind('<Double-Button-1>', lambda event: print(listbox.curselection()))

root.mainloop()