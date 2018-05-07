#-*-coding:utf-8 -*-
import sys
sys.path.append("...文件路径...")
import test2
from numpy import *
dataSet, labels = test2.createDataSet()
input = array([1.1, 0.3])
K = 3
output = test2.classify(input, dataSet, labels, K)
print("测试数据为:", input, "分类结果为：", output)
