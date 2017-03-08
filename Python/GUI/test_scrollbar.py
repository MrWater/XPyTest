import tkinter


root = tkinter.Tk()

s = tkinter.Scrollbar(root, orient=tkinter.HORIZONTAL)
s.set(0.5, 1)
s.pack()

# command一般用于和控件绑定，例如commnand=listbox.yview和listbox.yscrollcommand=s.set

root.mainloop()