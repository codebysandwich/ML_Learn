# -*- encoding: utf-8 -*-
'''
@Author: sandwich
@Date: 2020-09-15 17:13:12
@LastEditTime: 2020-09-15 17:13:14
@LastEditors: sandwich
@Description: KNN module
@FilePath: /ML_Learn/Machine_Learning_In_Action/KNN.py
'''

import os
import numpy as np
import operator

def createDataSet():
    """[summary]
    create dataset
    Returns:
        [tuple]: [group, labels]
    """
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classfiy0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqdiffMat = diffMat ** 2
    sqDistances = sqdiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDisIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDisIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), 
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def classfiy1(inX, dataSet, labels, k):
    if len(inX) == dataSet.shape[1]:
        distances = np.sqrt(np.sum((dataSet - inX) ** 2, axis=1))
        indicies = distances.argsort()
        classCount = {}
        for i in range(k):
            voteIlabel = labels[indicies[i]]
            classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.items(), 
                              key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]


if __name__ == "__main__":
    group, labels = createDataSet()
    # print(classfiy0([0, 0], group, labels, 3))
    print(classfiy1([0, 0], group, labels, 3))