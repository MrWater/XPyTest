arr = (1, 2, 3, 4)

# 递归实现 打印所有子集
def getAllCombination1(start = 0, s = ""):
	s += str(arr[start])
	print(s)

	if start + 1 >= len(arr):
		return

	getAllCombination1(start + 1, s)
	s = s[:-1]
	getAllCombination1(start + 1, s)

# 递归打印所有不重复的数字组成
visited = [False, False, False, False]
def getAllCombination2(start = -1, s = ""):
	flag = True
	print(s)

	for i in range(len(arr)):
		if(i == start or visited[i]):
			continue

		flag = False
		visited[i] = True
		getAllCombination2(start, s + str(arr[i]))
		visited[i] = False

	# if flag:
	# 	print(s)

# 迭代打印所有子集
def getAllCombination3():
	cnt = 2 ** len(arr)

	for i in range(1, cnt):
		s = ""

		for j in range(len(arr)):
			temp = i
			i >>= 1
			# print(str(temp) + " " + str(i))
			# print(i)
			temp ^= (i << 1)
			# print(temp)
			if temp == 1:
				s += str(arr[j])

		print(s)

getAllCombination3()


