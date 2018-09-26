import numpy as np
from sklearn import tree
import thrift
import graphviz 
#大为1，红为1，圆形为1, 好果为1
data = np.array([[1,1,1,1],
        [1,1,0,1],
        [1,1,1,1],
        [1,0,1,0],
        [1,0,1,0],
        [0,1,1,1],
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,0]])
clf = tree.DecisionTreeClassifier()
clf.fit(data[:,0:3],data[:,3])
dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=["magnitude","color","shape"],  
                         class_names=["bad","good"],  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)
graph.render("tree") 