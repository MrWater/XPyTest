# !/user/bin/python
# -*-coding:utf8-*-

from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as ptl

img = Image.open(r'C:\Users\WX\Desktop\test.jpg').convert('RGBA')
txt = Image.new('RGBA', img.size, (0,0,0,0))
fnt = ImageFont.truetype('c:/Windows/fonts/Tahoma.ttf', 20)
d = ImageDraw.Draw(txt)
d.text((txt.size[0]-80,txt.size[1]-30),'fsadfadf',font=fnt,fill=(255,255,255,255))
out = Image.alpha_composite(img,txt)
out.show()