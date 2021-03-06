import tkinter


root = tkinter.Tk()

tkinter.Button(root, text='Exit', command=root.quit).pack()

tkinter.Button(root, text='hello', command=lambda: print('hello')).pack()
tkinter.Button(root, text='aaa', relief=tkinter.FLAT).pack()

tkinter.Button(root,text='FLAT',relief=tkinter.FLAT).pack()
tkinter.Button(root,text='GROOVE',relief=tkinter.GROOVE).pack()
tkinter.Button(root,text='RAISED',relief=tkinter.RAISED).pack()
tkinter.Button(root,text='RIDGE',relief=tkinter.RIDGE).pack()
tkinter.Button(root,text='SOLID',relief=tkinter.SOLID).pack()
tkinter.Button(root,text='SUNKEN',relief=tkinter.SUNKEN).pack()

# image 使用PhotoImage(root, file=filepath)
# bitmap 使用X11格式的bitmap,windows的bitmap无法显示

# BITMAP = """
# #define im_width 32
# #define im_height 32
# static char im_bits[] = {
# 0xaf,0x6d,0xeb,0xd6,0x55,0xdb,0xb6,0x2f,
# 0xaf,0xaa,0x6a,0x6d,0x55,0x7b,0xd7,0x1b,
# 0xad,0xd6,0xb5,0xae,0xad,0x55,0x6f,0x05,
# 0xad,0xba,0xab,0xd6,0xaa,0xd5,0x5f,0x93,
# 0xad,0x76,0x7d,0x67,0x5a,0xd5,0xd7,0xa3,
# 0xad,0xbd,0xfe,0xea,0x5a,0xab,0x69,0xb3,
# 0xad,0x55,0xde,0xd8,0x2e,0x2b,0xb5,0x6a,
# 0x69,0x4b,0x3f,0xb4,0x9e,0x92,0xb5,0xed,
# 0xd5,0xca,0x9c,0xb4,0x5a,0xa1,0x2a,0x6d,
# 0xad,0x6c,0x5f,0xda,0x2c,0x91,0xbb,0xf6,
# 0xad,0xaa,0x96,0xaa,0x5a,0xca,0x9d,0xfe,
# 0x2c,0xa5,0x2a,0xd3,0x9a,0x8a,0x4f,0xfd,
# 0x2c,0x25,0x4a,0x6b,0x4d,0x45,0x9f,0xba,
# 0x1a,0xaa,0x7a,0xb5,0xaa,0x44,0x6b,0x5b,
# 0x1a,0x55,0xfd,0x5e,0x4e,0xa2,0x6b,0x59,
# 0x9a,0xa4,0xde,0x4a,0x4a,0xd2,0xf5,0xaa
# };
# """
# bmp = BitmapImage(data = BITMAP)
# Button(root, bitmap = bmp).pack()

# compound 图像的位置
# bd 设置border宽度
# state normal,active,disabled
# StringVar变量改变，相应绑定的值也改变,与Button的textvariable绑定

b = tkinter.Button(root, text='btn1', bd=1)
b.pack()
b.bind('<Return>', lambda event: print('focus'))

root.mainloop()