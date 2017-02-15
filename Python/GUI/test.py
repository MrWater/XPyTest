from tkinter import *

def showDialog():
	win = Toplevel()
	Label(win, text="这是一个对话框").pack()
	Button(win, text="退出", command=win.destroy).pack()
	win.focus_set()
	win.grab_set()
	win.wait_window()

root = Tk()
Entry(root, text="输入").pack()
Button(root, text="点击", command=showDialog).pack()
root.mainloop()


