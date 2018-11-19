# /bin/python3
# -*- coding:utf8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

__author__ = 'paif'

def autoNorm(dataSet):
    maxNum = dataSet.iloc[:, :3].max()
    minNum = dataSet.iloc[:, :3].min()
    labels = dataSet.iloc[:, -1]


def classify1(inX, dataSetPath, k):
    
    inX = np.array(inX)
    dataSet = pd.read_table(dataSetPath)
    k = int(k)

    # distance
    rowNum = dataSet.shape[0]
    distance = ((np.tile(inX, (rowNum, 1)) - dataSet) ** 2).sum(axis=1) ** 0.5
    labels = dataSet.iloc[:, -1]
    new_df = pd.DataFrame({'distance':distance, 'labels': labels})
    
    # sorted by distance, and split k
    new_df_01 = new_df.sort_index(by='distance')[:k]
    
    # count labels's numbers
    new_Series = new_df_01.count_values()

    # return index's name
    return new_Series.index[0]
