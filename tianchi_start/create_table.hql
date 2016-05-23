CREATE EXTERNAL TABLE `tmp_fresh_user`(
  `user_id` string,
  `item_id` string,
  `behavior_type` string,
  `user_geohash` string,
  `item_category` string,
  `behavior_time` string)
ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  'hdfs://public-namenode001-vnetz:9000/data/input/practice/tmp_fresh_user';


CREATE EXTERNAL TABLE `tmp_fresh_item`(
  `item_id` string,
  `item_geohash` string,
  `item_category` string)
ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  'hdfs://public-namenode001-vnetz:9000/data/input/practice/tmp_fresh_item';