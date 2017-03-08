from tkinter import *
root = Tk()
panes = PanedWindow(orient = VERTICAL)
panes.pack(fill = BOTH,expand = 1)
for w in [Label,Button,Checkbutton,Radiobutton]:
	panes.add(w(panes,text = 'hello'))
root.mainloop()
#每个pane 中创建一个widget