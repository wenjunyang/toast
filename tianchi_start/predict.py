#!/usr/bin/python2
# -*-coding:utf-8-*-
from __future__ import division
from datetime import datetime
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

__author__ = 'wendale'

_USER = 'data/tianchi_fresh_comp_train_user.csv'
_ITEM = 'data/tianchi_fresh_comp_train_item.csv'


# user = pd.read_csv(_USER)
# print user['user_id'].unique().size
# print user['item_id'].unique().size
#
# item = pd.read_csv(_ITEM)
# print item['item_id'].unique().size
# print item['item_category'].unique().size


# 将日期字符串转换为从基准日期的索引形式，
# 比如base_date_str = '2016-03-14'
# date_str = '2016-03-15 18' 则会返回(1, 18)
def transform_date(base_date_str, date_str):
    base_date = datetime.strptime(base_date_str, '%Y-%m-%d')
    the_date = datetime.strptime(date_str, '%Y-%m-%d %H')
    return (the_date - base_date).days, the_date.hour


def cal_f1(prediction_set, reference_set):
    intersection = prediction_set & reference_set
    precision = len(intersection) / len(prediction_set)
    recall = len(intersection) / len(reference_set)
    return 2 * precision * recall / (precision + recall)


def execute():
    train = pd.read_csv("data/train.csv")
    test = pd.read_csv("data/test.csv")
    clf = RandomForestClassifier(n_estimators=10)
    clf.fit(train.iloc[:,0:-1], train.iloc[:,-1])
    print clf.classes_
    p = clf.predict(test)

    with open('result.csv', 'w') as target:
        target.writelines('user_id,item_id\n')
        for i in range(len(test)):
            if p[i] > 0:
                target.writelines(str(test.iloc[i, 0]) + ',' + str(test.iloc[i, 1]) + '\n')

if __name__ == '__main__':
    execute()






