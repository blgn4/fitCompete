from influxdb import InfluxDBClient
import time
import random


client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')
start_time=time.time()
que = "select mean(speed),mean(calories_rate),mean(heart_rate) from week3_try1  where date='16-06-2016' group by user_id"
res = client.query(que)
res1= res.raw
series=res1['series']
count=0
redis_client = redis.StrictRedis(host='ec2-52-40-47-83.us-west-2.compute.amazonaws.com', port=6379, db=0,password='')
pipe = redis_client.pipeline()
for val in series:
	vals=val['values'][0]
	tags=val['tags']
	user_id=tags['user_id']
	speed=vals[0]
	calories_rate=vals[1]
	heart_rate=vals[2]
	bmi=random.randrange(18,35)
	fat=random.randrange(15,25)
	steps=random.randrange(1000,10000)
	floors=random.randrange(0,25)
	calories=random.randrange(1500,3000)
	period=random.randrange(0,3)
	data2=[bmi,calories,calories_rate,fat,floors,heart_rate,period,speed,steps]
	key='user:'+i[0]
	redis_client.delete(key)
	pipe.lpush(key,*data2)
	count +=1
	if count == 100000:
		pipe.execute()
		pipe = redis_client.pipeline()
		count=0


print("--- %s seconds ---" % (time.time() - start_time))