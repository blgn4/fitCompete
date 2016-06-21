from pyspark import SparkContext, SparkConf
from influxdb import InfluxDBClient
import redis
import time

redis_client = redis.StrictRedis(host='ec2-52-40-47-83.us-west-2.compute.amazonaws.com', port=6379, db=0,password='')

def get_data_from_influx():
	str2=[]
	user_list=redis_client.keys('*user*')
	for user in user_list:
		val=redis_client.lrange(user,0,-1)
		str1=''		
		bmi=int(val[0])
		if bmi <24:
			str1+='L'
		elif bmi>=24 and bmi<30:
			str1+='M'
		else:
			str1+='H'
		
		calories=int(val[1])
		if calories < 2000:
			str1+='L'
		elif calories >= 2000 and calories <=2500:
			str1+='M'
		else:
			str1+='H'
		
		calories_rate=float(val[2])
		if calories_rate < 8:
			str1+='L'
		elif calories_rate >= 8 and calories_rate <=9:
			str1+='M'
		else:
			str1+='H'

		fat=int(val[3])
		if fat < 18:
			str1+='L'
		elif fat >= 18 and calories_rate <=21:
			str1+='M'
		else:
			str1+='H'

		floors=int(val[4])
		if floors < 8:
			str1+='L'
		elif floors >=8 and floors <= 16:
			str1+='M'
		else:
			str1+='H'

		heart_rate=float(val[5])
		if heart_rate < 107:
			str1+='L'
		elif heart_rate>=107 and heart_rate <= 153:
			str1+='M'
		else:
			str1+='H'

		speed=float(val[6])
		if speed < 4:
			str1+='L'
		elif speed >=4 and speed <5:
			str1+='M'
		else:
			str1+='H'

		steps=int(val[8])
		if steps <3000:
			str1+='L'
		elif steps >= 3000 and steps <= 6000:
			str1+='M'
		else:
			str1+='H'

		period=int(val[6])
		if period==0:
			str1+='M'
		elif period==1:
			str1+='A'
		elif period==2:
			str1+='E'

		user_id=user.split(':')[1]
		str1+=','
		str1+=user_id
		str2.append(str1)
	return str2

def split_string(s):
	tup = s.split(',')
	return (tup[0],[tup[1]])

def write_into_redis(s):
	redis_client = redis.StrictRedis(host='ec2-52-40-47-83.us-west-2.compute.amazonaws.com', port=6379, db=0,password='')
	pipe = redis_client.pipeline()
	for i in s:
		redis_client.delete(*i[0])
		pipe.lpush(i[0],*i[1])
	pipe.execute()
	



appName='Similarity_APP'
master='spark://ec2-50-112-193-115.us-west-2.compute.amazonaws.com:7077'
conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)
start_time = time.time()
list_1 = get_data_from_influx()

print("--- %s seconds ---" % (time.time() - start_time))
rdd = sc.parallelize(list_1)

tupls=rdd.map(split_string)

buckets=tupls.reduceByKey(lambda a,b: a+b)
write_into_redis.count=0
buckets.foreachPartition(write_into_redis)














