import numpy as np
import matplotlib.pyplot as plt
import time

from sklearn import tree
# 按照一定规律均匀分布含有两个特征的数据点


def createData(samplecnt, coef=1.0, intercept=0.05):
    x1 = np.random.uniform(0, 1, samplecnt)
    x2 = np.random.uniform(0, 1, samplecnt)
    index = (x2 - intercept) / x1 < coef
    x1_pos = x1[index]
    x2_pos = x2[index]
    index = (x2 - intercept) / x1 >= coef
    x1_neg = x1[index]
    x2_neg = x2[index]
    # plt.xlabel("w1")
    # plt.ylabel("w2")
    # plt.scatter(x1_pos, x2_pos)
    # plt.scatter(x1_neg, x2_neg)
    # regx = np.linspace(0, 1, samplecnt)
    # regy = coef * regx + intercept
    # plt.plot(regx,regy,color='g')
    #plt.show()
    return x1_pos, x1_neg, x2_pos, x2_neg
# 组合成原始数据


def combine_data(x1_pos, x1_neg, x2_pos, x2_neg):
    x1_pos_1 = x1_pos.reshape(-1, 1)
    x2_pos_1 = x2_pos.reshape(-1, 1)
    x_pos = np.concatenate((x1_pos_1, x2_pos_1), axis=1)
    x_pos_shape = np.shape(x_pos)
    y_pos = np.ones(x_pos_shape[0])
    y_pos = y_pos.reshape(-1, 1)
    data_pos = np.concatenate((x_pos, y_pos, np.ones(len(x_pos)).reshape(-1, 1)), axis=1)
    # print(data_pos)
    x1_neg_1 = x1_neg.reshape(-1, 1)
    x2_neg_1 = x2_neg.reshape(-1, 1)
    x_neg = np.concatenate((x1_neg_1, x2_neg_1, np.ones(len(x1_neg_1)).reshape(-1, 1)), axis=1)
    x_neg_shape = np.shape(x_neg)
    y_neg = np.zeros(x_neg_shape[0])
    y_neg = y_neg.reshape(-1, 1)
    data_neg = np.concatenate((x_neg, y_neg), axis=1)
    data = np.vstack((data_pos, data_neg))
    data = np.random.permutation(data)

    return data

# b = np.ones(200)
'将偏移量与2个特征值组合 shape = (200,3)'
# X = np.hstack((b, X))


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def model(theta, X):
    theta = np.array(theta)
    return sigmoid(X.dot(theta))


def cost(m, theta, X, y):
    ele = y * np.log(model(theta, X)) + (1 - y) * np.log(1 - model(theta, X))
    item_sum = np.sum(ele)
    return -item_sum / m


def gradient(m, theta, X, y, cols):
    grad_theta = []
    for j in range(cols):
        grad = (model(theta, X) - y).dot(X[:, j])
        grad_sum = np.sum(grad)
        grad_theta.append(grad_sum / m)
    return np.array(grad_theta)
'theta update'


def theta_update(grad_theta, theta, sigma):
    return theta - sigma * grad_theta
'stop stratege'


def stop_stratege(cost, cost_update, threshold):
    return cost - cost_update < threshold
'逻辑回归算法'


def LogicRegression(X, y, threshold, m, xcols):
    start = time.clock()
    '设置权重参数的初始值'
    theta = np.zeros(xcols)
    '迭代步数'
    iters = 0
    '记录代价函数的值'
    cost_record = []
    '学习率'
    sigma = 0.5
    cost_val = cost(m, theta, X, y)
    cost_record.append(cost_val)
    while True:
        grad = gradient(m, theta, X, y, xcols)
        '参数更新'
        theta = theta_update(grad, theta, sigma)
        cost_update = cost(m, theta, X, y)
        if stop_stratege(cost_val, cost_update, threshold):
            break
        iters = iters + 1
        cost_val = cost_update
        # print("cost_val:%f" % cost_val)
        cost_record.append(cost_val)
    end = time.clock()
    print("LogicRegressionconvergence duration: %f s" % (end - start))
    return cost_record, iters, theta

x1_pos, x1_neg, x2_pos, x2_neg = createData(120)
data = combine_data(x1_pos, x1_neg, x2_pos, x2_neg)
# cost_record, iters, theta = LogicRegression(data[:, [0, 1, 2]], data[:, 3], 0.000001, 200, 3)

# plt.scatter(x1_pos, x2_pos)
# plt.scatter(x1_neg, x2_neg)
# wp = np.linspace(0.0, 1.0, 200)
# plt.plot(wp, -(theta[2] + theta[0] * wp) / theta[1], color='g')
# plt.show()

def decisionTreeBoundary(data,n_classes=2,plot_colors = "yb",plot_step = 0.02):
    #特征的列index
    pairidx,pair = [1,2],[1,2]
    X = data[:,[1,2]]
    y = data[:,3]
    # Train
    #构造的无参数构造函数
    clf = tree.DecisionTreeClassifier()
    clf.fit(X, y)
    # 绘制决策边界
    x_min, x_max = X[:, 0].min(), X[:, 0].max()
    y_min, y_max = X[:, 1].min(), X[:, 1].max()
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.BrBG)
    # 绘制训练点
    for i, color in zip(range(n_classes), plot_colors):
        idx = np.where(y == i)
        clabel=np.array(i,dtype=np.str)
        plt.scatter(X[idx, 0], X[idx, 1], c=color,label = clabel,
                   cmap=plt.cm.RdYlBu, edgecolor='black', s=15)

    plt.legend(loc='lower right', borderpad=0, handletextpad=0)
    plt.axis("tight")
    plt.xlabel("w1")
    plt.ylabel("w2")
    plt.title("using decision tree to binary classification")
    plt.show()

decisionTreeBoundary(data)