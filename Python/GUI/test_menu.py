import tkinter


root = tkinter.Tk()

menu = tkinter.Menu(root)
filemenu = tkinter.Menu(menu, tearoff=0)

for item in ['Python', 'PHP', 'CPP']:
	filemenu.add_command(label=item, command=lambda: print('点击'))
	filemenu.add_separator()

menu.add_cascade(label='Language', menu=filemenu)
root['menu'] = menu

menubar = tkinter.Menu(root)
def printItem():
	print('popup menu')
filemenu = tkinter.Menu(menubar,tearoff = 0)
for k in ['Python','PHP','CPP','C','Java','JavaScript','VBScript']:
	filemenu.add_command(label = k,command = printItem)
filemenu.add_separator()
menubar.add_cascade(label = 'Language',menu = filemenu)
#此时就不要将root 的menu 设置为menubar 了
#root['menu'] = menubar
def popup(event):
#显示菜单
	menubar.post(event.x_root,event.y_root)
#在这里相应鼠标的右键事件，右击时调用popup,此时与菜单绑定的是root，可以设置为
# 其它的控件，在绑定的控件上右击就可以弹出菜单
root.bind('<Button-3>',popup)

root.mainloop()