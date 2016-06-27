from influxdb import InfluxDBClient
import time
import random
import redis


client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')
start_time=time.time()
date= datetime.datetime.now()-datetime.timedelta(days=1)
que = "select mean(speed),mean(calories_rate),mean(heart_rate) from fit_timeseries where date="+date+" group by user_id "
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
	speed=str(vals[1])
	calories_rate=str(vals[2])
	heart_rate=str(vals[3])
	bmi=str(random.randrange(18,35))
	fat=str(random.randrange(15,25))
	steps=str(random.randrange(1000,10000))
	floors=str(random.randrange(0,25))
	calories=str(random.randrange(1500,3000))
	period=str(random.randrange(0,3))
	data2=[steps,speed,period,heart_rate,floors,fat,calories_rate,calories,bmi]
	key='user:'+user_id
	redis_client.delete(*key)
	pipe.lpush(key,*data2)
	count +=1
	pipe.execute()


print("---aggregates calculated in %s seconds ---" % (time.time() - start_time))