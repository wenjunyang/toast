CREATE EXTERNAL TABLE `stg_ssq`(
  `id` string,
  `red1` int, 
  `red2` int, 
  `red3` int,
  `red4` int,
  `red5` int,
  `red6` int,
  `blue` int
  )
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ',' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  'hdfs://dev-hadoop-md01-v-o:9000/data/bi/stg/stg_ssq';
  
  
-- 篮球频率
select blue,
       count(*) as cnt,
       count(*) / sum(count(*)) over () as frequency
  from stg_ssq
 group by blue
 order by frequency desc;
  
-- 红球频率
select red,
       count(*) as cnt,
       count(*) / sum(count(*)) over () as frequency
  from
    (
        select stack(6, red1, red2, red3, red4, red5, red6) as red
          from stg_ssq
    ) v
group by red
order by frequency desc

