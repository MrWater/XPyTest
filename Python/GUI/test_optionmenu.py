import tkinter


root = tkinter.Tk()

v = tkinter.StringVar()
v.set('python')
optionmenu = tkinter.OptionMenu(root, v, 'python', 'ph', 'ff')
optionmenu.pack()

root.mainloop()