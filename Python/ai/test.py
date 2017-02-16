# !/user/bin/python
# -*-coding:utf8-*-

__author__ = 'wx'

import numpy as np
import uuid
import matplotlib.pyplot as ptl

from PIL import Image # library for processing image

image_path = './imgs/'
num = 100

img = Image.open(image_path + str(np.random.randint(num)) + ".jpg").convert('L')

ptl.figure('captcha')

ptl.subplot(3,5,1)
ptl.imshow(img)
ptl.title(u'原图', fontproperties='SimHei')

ptl.subplot(3,5,6)
ptl.imshow(img, cmap='gray')
ptl.title(u'灰度', fontproperties='SimHei')


img_arr = np.array(img)

rows,cols = img_arr.shape
for i in range(rows):
	for j in range(cols):
		if img_arr[i,j] <= 127:
			img_arr[i,j] = 0
		else:
			img_arr[i,j] = 255

min_x = cols 
min_y = rows 
max_x = max_y = 0

for i in range(rows):
	for j in range(cols):
		if img_arr[i,j] == 0: 
			if i < min_y:
				min_y = i
			if j < min_x:
				min_x = j

			if i > max_y:
				max_y = i
			if j > max_x:
				max_x = j 

max_x += 1
max_y += 1
box = (min_x, min_y, max_x, max_y)
img = Image.fromarray(img_arr)

ptl.subplot(3,5,11)
ptl.imshow(img, cmap='gray')
ptl.title(u'二值化', fontproperties='SimHei')

img = img.crop(box)
img_arr = np.array(img)

d = 0
d1 = d2 = d3 = d4 = d5 = d6 = 0
flag = False # 是否在黑色列
flag2 = False # 控制白色列前进

for i in range(max_x-min_x): 
	flag = False

	for j in range(max_y-min_y):
		if img_arr[j,i] == 0:
			flag = True
			break

	print(flag)
	if flag: #说明在黑色
		if not flag2: # 如果刚才在黑色列，说明一直处于黑色列，不管，否则说明由白色进入黑色，开始记录
			pass
		else:
			d += 1

			if d == 2:
				d2 = i
			elif d == 4:
				d4 = i
			elif d == 6:
				d6 = i

			flag2 = False


	else: # 说明在白色
		if not flag2: # 由黑色列进入白色
			d += 1
			
			if d == 1:
				d1 = i
			elif d == 3:
				d3 = i
			elif d == 5:
				d5 = i

			flag2 = True
		
print(d1, d2, d3, d4, d5, d6)

# ptl.figure('captcha')

# ptl.subplot(2,3,1)
# ptl.imshow(img, cmap='gray')
# ptl.title(u'原数', fontproperties='SimHei')
# 

# ptl.subplot(2,3,2)
# ptl.imshow(img.crop((0, 0, w, max_y-min_y)), cmap='gray')
# ptl.title('first')
# 

# ptl.subplot(2,3,3)
# ptl.imshow(img.crop((w+d, 0, d+2*w, max_y-min_y)), cmap='gray')
# ptl.title('second')
# 

# ptl.subplot(2,3,5)
# ptl.imshow(img.crop((2*d+2*w, 0, 3*w+2*d, max_y-min_y)), cmap='gray')
# ptl.title('third')
# 

# ptl.subplot(2,3,6)
# ptl.imshow(img.crop((3*d+3*w, 0, 4*w+3*d, max_y-min_y)), cmap='gray')
# ptl.title('fourth')
# 

# ptl.show()

# 加载已有数字模板，分析特征值
eigenvalue = [] # 字典保存数字对应的图片像素值
for t in range(10):
	arr = np.array(Image.open('./' + str(t) + '.jpg'))
	rows,cols = arr.shape
	for i in range(rows):
		for j in range(cols):
			if arr[i,j] <= 200:
				arr[i,j] = 0
			else:
				arr[i,j] = 255

	eigenvalue.append([arr, t])

# ptl.subplot(3,5,12)
# ptl.title(u'模板', fontproperties='Simhei')
# 
# for i in eigenvalue:
# 	ptl.imshow(Image.fromarray(i[0]), cmap='gray')

# 分割四个数字进行匹配

ptl.subplot(3,5,2)
ptl.imshow(img.crop((0, 0, d1, max_y-min_y)), cmap='gray')
ptl.title(u'原数', fontproperties='SimHei')


img_arr = np.array(img.crop((0, 0, d1, max_y-min_y)))
rows,cols = img_arr.shape

max_match = 0
for v in eigenvalue:
	cnt = 0
	rows = min((rows, v[0].shape[0]))
	cols = min((cols, v[0].shape[1]))
	pixel_sum = rows * cols

	for i in range(rows):
		for j in range(cols):
			if img_arr[i,j] == v[0][i,j]:
				cnt += 1

	if cnt / pixel_sum > max_match :
		max_match = cnt / pixel_sum
		value = v

ptl.subplot(3,5,7)
ptl.imshow(Image.fromarray(value[0]), cmap='gray')
ptl.title(u'识别:' + str(value[1]), fontproperties='SimHei')

ptl.subplot(3,5,3)
ptl.imshow(img.crop((d2, 0, d3, max_y-min_y)), cmap='gray')
ptl.title(u'原数', fontproperties='SimHei')

img_arr = np.array(img.crop((d2, 0, d3, max_y-min_y)))
rows,cols = img_arr.shape

max_match = 0
for v in eigenvalue:
	cnt = 0
	rows = min((rows, v[0].shape[0]))
	cols = min((cols, v[0].shape[1]))
	pixel_sum = rows * cols

	for i in range(rows):
		for j in range(cols):
			if img_arr[i,j] == v[0][i,j]:
				cnt += 1

	if cnt / pixel_sum > max_match:
		max_match = cnt / pixel_sum
		value = v

ptl.subplot(3,5,8)
ptl.imshow(Image.fromarray(value[0]), cmap='gray')
ptl.title(u'识别:' + str(value[1]), fontproperties='SimHei')



ptl.subplot(3,5,4)
ptl.imshow(img.crop((d4, 0, d5, max_y-min_y)), cmap='gray')
ptl.title(u'原数', fontproperties='SimHei')


img_arr = np.array(img.crop((d4, 0, d5, max_y-min_y)))
rows,cols = img_arr.shape

max_match = 0
for v in eigenvalue:
	cnt = 0
	rows = min((rows, v[0].shape[0]))
	cols = min((cols, v[0].shape[1]))
	pixel_sum = rows * cols

	for i in range(rows):
		for j in range(cols):
			if img_arr[i,j] == v[0][i,j]:
				cnt += 1

	if cnt / pixel_sum > max_match:
		max_match = cnt / pixel_sum
		value = v
ptl.subplot(3,5,9)
ptl.imshow(Image.fromarray(value[0]), cmap='gray')
ptl.title(u'识别:' + str(value[1]), fontproperties='SimHei')



ptl.subplot(3,5,5)
ptl.imshow(img.crop((d6, 0, max_x-min_x, max_y-min_y)), cmap='gray')
ptl.title(u'原数', fontproperties='SimHei')


img_arr = np.array(img.crop((d6, 0, max_x-min_x, max_y-min_y)))
rows,cols = img_arr.shape

max_match = 0
for v in eigenvalue:
	cnt = 0
	rows = min((rows, v[0].shape[0]))
	cols = min((cols, v[0].shape[1]))
	pixel_sum = rows * cols

	for i in range(rows):
		for j in range(cols):
			if img_arr[i,j] == v[0][i,j]:
				cnt += 1

	if cnt / pixel_sum > max_match:
		max_match = cnt / pixel_sum
		value = v
ptl.subplot(3,5,10)
ptl.imshow(Image.fromarray(value[0]), cmap='gray')
ptl.title(u'识别:' + str(value[1]), fontproperties='SimHei')


ptl.show()

# img.crop((0, 0, d1, max_y-min_y)).convert('1').save('./' + str(uuid.uuid1()) + '.jpg')
# img.crop((d2, 0, d3, max_y-min_y)).convert('1').save('./' + str(uuid.uuid1()) + '.jpg')
# img.crop((d4, 0, d5, max_y-min_y)).convert('1').save('./' + str(uuid.uuid1()) + '.jpg')
# img.crop((d6, 0, max_x-min_x, max_y-min_y)).convert('1').save('./' + str(uuid.uuid1()) + '.jpg')

