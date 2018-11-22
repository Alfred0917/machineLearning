#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
朴素贝业斯在本例中的应用就是判断当文档包含粗鲁单词的时候会分到哪一类;
p0 = 正常文档
p1 = 垃圾文档
p(rude/1) = 垃圾文档中出现rude单词的概率
p(rude) = 所有单词中rude单词出现的概率
求p(1/rude)出现rude单词时，文件是粗鲁文档的概率
公式: p(1/rude) = (p(rude/1)*p1) / p(rude)
"""


def loadDataSet():
    """
    创建数据集
    :return: 单词列表postingList, 所属类别classVec
    """
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # [0,0,1,1,1......]
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec


def createVocabList(dataSet):
    vocab = []
    for data in dataSet:
        vocab.extend(data)
    vocabList = list(set(vocab))
    return vocabList


def probability(dataSet, classVec):
    p1 = sum(classVec) / len(classVec)
    # p0 = (len(classVec) - sum(classVec)) / len(classVec)

    pass


dataSet, classVec = loadDataSet()
print(createVocabList(dataSet))
