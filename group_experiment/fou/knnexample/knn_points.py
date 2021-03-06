# coding:utf-8
# -*- coding : gbk -*-

from numpy import *
import pickle

"""
Knn方法的测试样本
"""

# Knn分类器的类定义


class KnnClassifier(object):

    def __init__(self, labels, samples):
        """ Initialize classifier with training data. """

        self.labels = labels
        self.samples = samples

    def classify(self, point, k=3):
        """ Classify a point against k nearest 
            in the training data, return label. """

        # compute distance to all training points
        dist = array([L2dist(point, s) for s in self.samples])

        # sort them
        ndx = dist.argsort()

        # use dictionary to store the k nearest
        votes = {}
        for i in range(k):
            label = self.labels[ndx[i]]
            votes.setdefault(label, 0)
            votes[label] += 1

        return max(votes)

# L2距离


def L2dist(p1, p2):
    return sqrt(sum((p1-p2)**2))

# L1距离


def L1dist(v1, v2):
    return sum(abs(v1-v2))


# 读入训练样本
with open(r'E:\study\Experiments\python_calu\group_experiment\fou\knnexample\points_ring.pkl') as fp:
    file_1 = fp.read()
    file_2 = bytes(file_1, 'ascii')
    class_1 = pickle.loads(file_2, encoding='bytes')
    class_2 = pickle.loads(file_2, encoding='bytes')
    labels = pickle.loads(file_2, encoding='bytes')

# 在训练样本集上获得Knn分类器
model = KnnClassifier(labels, vstack((class_1, class_2)))

# 读入测试样本
with open(r'E:\study\Experiments\python_calu\group_experiment\fou\knnexample\points_ring_test.pkl') as fp:
    file_1 = fp.read()
    file_2 = bytes(file_1, 'ascii')
    class_1 = pickle.loads(file_2, encoding='bytes')
    class_2 = pickle.loads(file_2, encoding='bytes')
    labels = pickle.loads(file_2, encoding='bytes')

# 在第一个测试样本上的分类结果
print(model.classify(class_1[0]))
