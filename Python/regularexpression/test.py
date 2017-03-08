# !/user/bin/env python
# -*- coding:utf-8 -*-


import re

s = 'fsfas法师法师打发ffsdffsd'
pattern = r'([\w]*)'

result = re.search(pattern, s)

if result:
	print(result.groups())