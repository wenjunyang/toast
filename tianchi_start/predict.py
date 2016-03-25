#!/usr/bin/python2
# -*-coding:utf-8-*-
from datetime import datetime
import pandas as pd

__author__ = 'wendale'

_USER = 'data/tianchi_fresh_comp_train_user.csv'
_ITEM = 'data/tianchi_fresh_comp_train_item.csv'


user = pd.read_csv(_USER)
print user['user_id'].unique().size

item = pd.read_csv(_ITEM)
print item['item_geohash']

# 将日期字符串转换为从基准日期的索引形式，
# 比如base_date_str = '2016-03-14'
# date_str = '2016-03-15 18' 则会返回(1, 18)
def transform_date(base_date_str, date_str):
    base_date = datetime.strptime(base_date_str, '%Y-%m-%d')
    the_date = datetime.strptime(date_str, '%Y-%m-%d %H')
    return ((the_date - base_date).days, the_date.hour)
