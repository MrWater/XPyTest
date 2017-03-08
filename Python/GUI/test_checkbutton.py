import tkinter


root = tkinter.Tk()

# IntVar StringVar DoubleVar

tkinter.Checkbutton(root, text='checkbutton').pack()
tkinter.Checkbutton(root, text='commnad', command=lambda: print('状态改变')).pack()

# checkbutton不仅仅是1或者0，还可以是其他值，通过onvalue和offvalue设置
tkinter.Checkbutton(root, text='on off', onvalue='on', offvalue='off').pack()

root.mainloop()