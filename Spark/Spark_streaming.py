import sys
from pyspark import SparkContext,SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import redis

def split_features(s):
    x=s[1].split(',')
    return (x[1],(int(x[3]), int(x[2]) ))

def split_count(s):
    x=s[1].split(',')
    return (x[1],1)

def window_sum_hr_speed(a,b):
	hr1=a[0]
	hr2=b[0]
	st1=a[1]
	st2=b[1]
	return (hr1+hr2,st1+st2)

def computations(s):
    hr_sum_=int(s[1][0][0])
    st_sum_=int(s[1][0][1])
    count_=int(s[1][1])
    #average heart rate
    hr_avg_=hr_sum_ / count_
    
    distance= (st_sum_ * 2.5) + 1

    if distance == 0 or distance == 1:
    	pace =0
    else:
    	pace= ((3 / distance) * 88.23)

    return (s[0],(round(hr_avg_,2), round(pace,2) ))

def save_to_redis(s):
	rediscon=redis.StrictRedis(host='ec2-52-40-47-83.us-west-2.compute.amazonaws.com', port=6379, db=0,password='')
	pipe = rediscon.pipeline()
	for i in s:
		key='stream'
		value=i[1]
		val=str(i[0])+','+str(value[0])+','+str(value[1])
		pipe.lpush(key,val)
	pipe.execute()


appName='Stream_APP'
master='spark://ec2-50-112-193-115.us-west-2.compute.amazonaws.com:7077'
conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)
ssc = StreamingContext(sc, 1)
ssc.checkpoint("hdfs://ec2-50-112-193-115.us-west-2.compute.amazonaws.com:9000/user/spark_checkpoint")
brokers="52.41.140.111:9092,52.41.90.5:9092,52.41.120.152:9092"
kvs = KafkaUtils.createDirectStream(ssc, ["stream_test"], {"metadata.broker.list": brokers})

user_metric = kvs.map(split_features)

user_count=kvs.map(split_count)

count_stream =  user_count.reduceByKeyAndWindow(lambda x, y: x + y, 3, 1)

sum_stream = user_metric.reduceByKeyAndWindow(window_sum_hr_speed, 3, 1)

joined_stream=sum_stream.join(count_stream)

smoothened_stream= joined_stream.map(computations)


smoothened_stream.foreachRDD(lambda rdd: rdd.foreachPartition(save_to_redis))

ssc.start()
ssc.awaitTermination()
