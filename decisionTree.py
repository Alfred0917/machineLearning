import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calcShannonEnt(dataSet):
    """
    计算香农熵
    :param dataSet: 最后一列为分类，其余列为特征
    :return: 香农熵（float）
    """
    labels = dataSet.iloc[:, -1]
    pi = labels.value_counts() / len(labels)
    shannonEnt = sum(- pi * np.log2(pi))
    return shannonEnt


def splitDataSet(dataSet, feature, value):
    """
    分割数据集
    :param dataSet: 数据集
    :param feature: 特征
    :param value: 特征值
    :return: 数据子集(DataFrame)
    """
    subDataSet = dataSet[dataSet[feature] == value]
    return subDataSet


def chooseBestFeature(dataSet):
    """
    选择分割数据集最优的特征
    :param dataSet:数据集
    :return: 最优的特征
    """
    baseEnt = calcShannonEnt(dataSet)
    featEntList = []
    for feature in dataSet.columns[:-1]:
        columnEnt = []
        for value in dataSet[feature].value_counts().index:
            subDataSet = splitDataSet(dataSet, feature, value)
            pi = len(subDataSet) / len(dataSet)
            subDataSetEnt = pi * calcShannonEnt(subDataSet)
            columnEnt.append(subDataSetEnt)
        featEntList.append(sum(columnEnt))
    featEnt = pd.Series(featEntList, index=dataSet.columns[:-1])
    infoGain = baseEnt - featEnt
    bestFeature = infoGain.idxmax()
    # print(bestFeature)
    return bestFeature


def myTrees(dataSet):
    bestFeature = chooseBestFeature(dataSet)
    print("当前选择的最优特征为:{}".format(bestFeature))
    values = dataSet[bestFeature].value_counts().index
    subDataList = []
    for value in values:
        subDataSet = splitDataSet(dataSet, bestFeature, value)
        print(subDataSet)
        subDataList.append(subDataSet)

    for subData in subDataList:
        if chooseBestFeature(subData) != bestFeature:
            myTrees(subData)
        elif chooseBestFeature(subData) == bestFeature:
            pass

    return subDataList


def createDataSet():
    data = [[1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']]
    labels = ['fly', 'meat', 'fish']
    dataSet = pd.DataFrame(data, columns=labels)
    return dataSet


dataSet = createDataSet()
myTrees(dataSet)
