-- 粗略预测,并计算准确度 召回率 F1
select precision,
       recall,
       2 * precision * recall / (precision + recall)
  from
(
    select sum(if(rn=2, 1, 0)) / sum(if(flag=1, 1, 0)) as precision,
           sum(if(rn=2, 1, 0)) / sum(if(flag=2, 1, 0)) as recall
      from
    (
        select user_id,
               item_id,
               flag,
               row_number() over (partition by user_id, item_id) as rn
          from
        (
            select s.user_id,
                   s.item_id,
                   1 as flag
              from
            (
                select distinct user_id,
                       item_id
                  from tmp_fresh_user u
                 where substr(behavior_time, 0, 10) in ('2014-12-15', '2014-12-16', '2015-12-17')
                   and behavior_type = 3
             ) s
             inner join tmp_fresh_item i
                     on s.item_id = i.item_id
            union all
            select s.user_id,
                   s.item_id,
                   2 as flag
              from
            (
                select distinct user_id,
                       item_id
                  from tmp_fresh_user
                 where substr(behavior_time, 0, 10) = '2014-12-18'
                   and behavior_type = 4
            ) s
            inner join tmp_fresh_item i
                     on s.item_id = i.item_id
        ) t1
    ) t2
) t3


-- 粗略预测
INSERT OVERWRITE LOCAL DIRECTORY '/home/ohonggh/bigteam/wenjun/fresh'
ROW FORMAT DELIMITED FIELDS TERMINATED BY','
select s.user_id,
       s.item_id
  from
(
select distinct user_id,
                 item_id
            from tmp_fresh_user u
           where substr(behavior_time, 0, 10) in ('2014-12-15', '2014-12-16', '2015-12-17', '2015-12-18')
             and behavior_type = 3
) s
inner join tmp_fresh_item i
  on s.item_id = i.item_id


--生成按以下特征
--用户,商品,浏览次数,收藏次数,加入购物车次数,是否购买
drop view if exists tmp_fresh_user_encode;
CREATE VIEW tmp_fresh_user_encode AS
SELECT u.user_id,
       u.item_id,
       u.behavior_type,
       u.user_geohash,
       u.item_category,
       datediff(substr(u.behavior_time, 0, 10), '2014-11-18') as date_index
  from tmp_fresh_user u
  left outer join tmp_fresh_item i
    on u.item_id = i.item_id
 where i.item_id is not null;

-- 窗口模板
select user_id,
       item_id,
       sum(if(behavior_type=1, 1, 0)) as click_times,
       sum(if(behavior_type=2, 1, 0)) as sava_times,
       sum(if(behavior_type=3, 1, 0)) as cart_times,
       sum(if(behavior_type=4 and date_index=3, 1, 0)) as buy_times
  from tmp_fresh_user_encode
 where date_index >= 0 and date_index <= 2
 group by user_id, item_id

 --测试数据模板
INSERT OVERWRITE LOCAL DIRECTORY '/home/ohonggh/bigteam/wenjun/test'
ROW FORMAT DELIMITED FIELDS TERMINATED BY','
select user_id,
   item_id,
   sum(if(behavior_type=1, 1, 0)) as click_times,
   sum(if(behavior_type=2, 1, 0)) as sava_times,
   sum(if(behavior_type=3, 1, 0)) as cart_times
from tmp_fresh_user_encode
where date_index >= 26 and date_index <= 30
group by user_id, item_id;





select * from
(
select user_id,
       item_id,
       sum(if(behavior_type=1 and date_index >= 3 and date_index <= 7, 1, 0)) as click_times,
       sum(if(behavior_type=2 and date_index >= 3 and date_index <= 7, 1, 0)) as sava_times,
       sum(if(behavior_type=3 and date_index >= 3 and date_index <= 7, 1, 0)) as cart_times,
       sum(if(behavior_type=4 and date_index=8, 1, 0)) as buy_times
  from tmp_fresh_user_encode
 group by user_id, item_id
) s
where buy_times > 0
