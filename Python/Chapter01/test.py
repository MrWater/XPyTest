from Entity.Base import *

file1 = "C:\\Users\\WX\\Desktop\\style.txt"
file2 = "style.txt"
dir1 = "C:\\Users\\WX\\Desktop"

print(os.path.split(file1))  #os.path.split分离目录和文件
print(os.path.splitext(file1))  #os.path.splittext分离文件后缀
print(os.path.normpath(file2)) #os.path.normpath绝对路径转相对路径
print(os.path.abspath(file2)) #os.path.abspath相对路径转绝对路径
print(sorted(os.listdir("C:\\Users\\wx\\Desktop"))) #os.listdir列出目录下的所有文件和子目录

mod_time = os.path.getmtime(dir1)
print(mod_time)
print(time.ctime(mod_time))

# shutil.move 移动文件
# shutil.copy 复制文件
# shutil.rmtree 删除目录，包括目录中的所有
# os.rename 重命名文件
# os.remove 删除文件
# os.unlink 删除文件，与remove功能一样
# os.mkdir 创建空目录，必须保证目录的路径存在
# os.makedirs 创建空目录，路径可以不存在（父目录可以不存在）
# os.rmdir 删除目录，仅针对空目录，若目录不空删除失败
# os.walk 遍历目录

# filter 为迭代器添加过滤器
# map 遍历集合每个条目，并对元素作相应改变

filter_me = [1,2,3,4,6,7,8,11,12,14,15,19,22]
# result = filter(lambda x: x % 2 == 0, filter_me)
# print(*result)

result = map(lambda x: "current:%d" % x, filter_me)
print(*result)

# 列表解析，用于限制被访问的元素范围，类似filter
everything = [1,2,3,4,5,6,7,8,9,10,11,12]
print([x*2 for x in everything if x%2 == 0])

f = range(10, 20)
print(*f) # range和map返回的都是集合数据，用*取得集合的值

# 字典的特殊字符串格式化
person = [{"name" : "James", "age" : 12, "height" : 178}, {"name" : "James", "age" : 12, "height" : 178}]
# print("%(name)s, %(age)d" % person)
# person["height"] = 178
# print("%s, %s" % (person["name"], person["age"]))

# t = string.Template($name is $height m hign\n");"
# print(t.substitute(person))

# result = map(lambda x: t.substitute(x), person)
# print(*result)

print(os.getcwd())

print(os.stat(file1))

result = filter((lambda x: re.search(r"[^c]*", x)), ('c', 'cc', 'ccx',))
print(*result)

