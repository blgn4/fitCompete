from pyspark import SparkContext, SparkConf
from influxdb import InfluxDBClient
import random
import time
import redis

appName='Similarity_APP'
master='spark://ec2-50-112-193-115.us-west-2.compute.amazonaws.com:7077'
conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)
client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')


def form_tuples(s):
	strg=s['values'][0]
	return (strg[1],strg[2])

def write_into_influx(s):
	redis_client = redis.StrictRedis(host='ec2-52-40-47-83.us-west-2.compute.amazonaws.com', port=6379, db=0,password='')
	pipe = redis_client.pipeline()
	for i in s:
		que = "select mean(speed),mean(calories_rate),mean(heart_rate) from week3_try1 where user_id='"+i[0]+"' and date='"+i[1]+"' group by user_id"
		res = client.query(que)
		res1= res.raw
		series=res1['series'][0]
		vals=series['values'][0]
		tags=series['tags']
		user_id=tags['user_id']
		speed=vals[1]
		calories_rate=vals[1]
		heart_rate=vals[2]
		bmi=random.randrange(18,35)
		fat=random.randrange(15,25)
		steps=random.randrange(1000,10000)
		floors=random.randrange(0,25)
		calories=random.randrange(1500,3000)
		data2=['bmi'+bmi,'calories'+calories,'CR'+calories_rate,'fat'+fat,'floors'+floors,'hr'+heart_rate,'speed'+speed,'steps'+steps]
		key='user:'+i[0]
		redis_client.delete(key)
		pipe.lpush(key,*data2)
	pipe.execute()

		
query='select user_id,last(date) from week3_try1 group by  user_id where time <= now() -1d'
result = client.query(query)
res=result.raw
count =0
series=res['series']
serie = series+series
raw_data=sc.parallelize(serie)

user_data=raw_data.map(form_tuples)

user_data.foreachPartition(write_into_influx)

