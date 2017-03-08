import tkinter 


root = tkinter.Tk()

text = tkinter.StringVar()
text.set("FDSFSDF")

entry = tkinter.Entry(root, textvariable=text, state='readonly')
entry.pack()
# entry['state']='readonly'
# 设置密码框 show控制 show='*'
def test(content,reason,name):
	if content == "舍名利":
		print('正确')
		print(content, reason,name)
		return True
	else:
		print('错误')
		print(content, reason,name)
		return False
testcmd = root.register(test)

# validate: all,key,focus,focusin,focusout,none
# %P 当前值 %v当前validate的值 %W 组件名字
tkinter.Entry(root, validate='focusout', validatecommand=(testcmd,'%P','%v','%W')).pack()


root.mainloop()