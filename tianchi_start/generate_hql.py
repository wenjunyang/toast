#!/usr/bin/python2
# -*-coding:utf-8-*-
import sys

hql_unit = """select user_id,
       item_id,
       sum(if(behavior_type=1 and %s, 1, 0)) as click_times,
       sum(if(behavior_type=2 and %s, 1, 0)) as sava_times,
       sum(if(behavior_type=3 and %s, 1, 0)) as cart_times,
       sum(if(behavior_type=4 and date_index=%d, 1, 0)) as buy_times
  from tmp_fresh_user_encode
 group by user_id, item_id"""

interval = 5

hql_list = []
for i in range(interval, 31):
    condition = 'date_index >= %d and date_index <= %d' % (i - interval, i - 1)
    hql_list.append(hql_unit % (condition, condition, condition, i))

print """INSERT OVERWRITE LOCAL DIRECTORY '/home/ohonggh/bigteam/wenjun/fresh'
ROW FORMAT DELIMITED FIELDS TERMINATED BY','"""

print '\nunion all\n'.join(hql_list) + ';'