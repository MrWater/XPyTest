import urllib.request
import os

#此处路径自己修改， 
path='./imgs/'
num=100

if __name__ == '__main__':
	if os.path.exists(path):  

	    pass
	else:

	    os.makedirs(path)
	for i in range(0,num):
	    print("下载第"+str(i)+"张验证码")
	    filePath=path+str(i)+'.jpg'
	    #这个地址下可以下载到普通的验证码
	    r=urllib.request.urlopen('http://jw.hrbeu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS')
	    with open(filePath,'bw') as f:
	        f.write(r.read())

