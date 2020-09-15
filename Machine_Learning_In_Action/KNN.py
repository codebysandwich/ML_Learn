# -*- encoding: utf-8 -*-
'''
@Author: sandwich
@Date: 2020-09-15 17:13:12
@LastEditTime: 2020-09-15 17:13:14
@LastEditors: sandwich
@Description: KNN module
@FilePath: /ML_Learn/Machine_Learning_In_Action/KNN.py
'''

import numpy as np

def createDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

if __name__ == "__main__":
    group, labels = createDataSet()
    print(group)
    print(labels)