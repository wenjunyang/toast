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
  
  
-- 篮球概率
select blue, count(*),  from stg_ssq group by blue  
  
  
  

