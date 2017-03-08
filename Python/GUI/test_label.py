from tkinter import *


root = Tk()

Label(root, bitmap='hourglass', bg='#FF00FF', width=10, height=10).pack()
Label(root, text='fsdf', bg='#FF00FF').pack()
Label(root, text='fsdf', bg='SystemActiveBorder').pack() # 支持与操作系统相关的颜色
Label(root, text='fsdf', bg='blue', justify='center').pack()

# 可用位图,error hourglass info questhead question warning gray12 gray25 gray50 gray75
# warplength 指定多少单位互殴开始换行
# justify 指定多行的对齐方式
# ahchor 指定文本或图像(bitmap, image) 显示位置
# nw n ne
# w center e
# sw s se

root.mainloop();