#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# 1.创建数据集
def create_data(data, labels):
    data = pd.DataFrame(data, columns=labels)
    return data


# 2.计算香农熵.公式 -p * log2(p)
def calc_shannon_entory(data):
    result = data.iloc[:, -1].value_counts()  # 取最后一列（结果列）
    sampleNums = len(data)  # 样本个数
    result_probability = result / sampleNums  # 计算概率
    shannon_entory = -sum(result_probability * np.log2(result_probability))
    return shannon_entory


# 3.选择bestFeature
def choose_best_feature(data):
    base_entory = calc_shannon_entory(data)
    # 遍历所有特征
    features = data.columns[:-1]
    feature_ents = []
    for feature in features:
        child_data_ent = 0
        values = data[feature].value_counts()
        for value in values.index:
            child_data = data[data[feature] == value]
            child_data_p = len(child_data) / len(data)
            child_data_ent += child_data_p * calc_shannon_entory(child_data)
        feature_ents.append(child_data_ent)
    feature_ents_details = pd.Series(feature_ents, index=features)
    info_gain = base_entory - feature_ents_details
    best_feature = info_gain.idxmax()
    print(best_feature)
    return best_feature


# 4.安装bestFeature分割数据集
def split_data(data, feature, value):
    child_data = data[data[feature] == value]
    return child_data


# 5.创建decision_tree
def creat_tree(data):
    features = list(data.columns[:-1])
    result = data.iloc[:, -1].value_counts()  # 最后一列
    if len(features) == 1 or len(result) == 1:
        return result.index[0]
    best_feature = choose_best_feature(data)
    my_tree = {best_feature: {}}
    features.remove(best_feature)
    values = data[best_feature].value_counts().index
    for value in values:
        my_tree[best_feature][value] = creat_tree(split_data(data, best_feature, value))

    return my_tree



data = create_data([[1, 1, 'yes'],
                    [1, 1, 'yes'],
                    [1, 0, 'no'],
                    [0, 1, 'no'],
                    [0, 1, 'no']],
                   ['no surfacing', 'flippers', 'fish'])

print(creat_tree(data))
