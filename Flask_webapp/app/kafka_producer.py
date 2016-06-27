import time
from kafka import KafkaProducer
import random
from time import sleep
import sys
import datetime
import redis

def stream_generator():
	rediscon=redis.StrictRedis(host='ec2-52-40-47-83.us-west-2.compute.amazonaws.com', port=6379, db=0,password='')
	producer = KafkaProducer(bootstrap_servers=["52.41.140.111:9092","52.41.90.5:9092","52.41.120.152:9092"])
	res = rediscon.get('active')
	tp=random.randrange(900000,1800001)
	st =  int(round(time.time() * 1000))
	diff=0
	while  True:
		if res==1 and diff==0:			
			tp=random.randrange(900000,1800001)
			st =  int(round(time.time() * 1000))

		if res == 1:
			diff = int(round(time.time() * 1000))- st
			st1=0 #steps
			st2=0
			u1=0  #user_id
			u2=1
			now=datetime.datetime.now()-datetime.timedelta(hours=7)
			hr1=random.randrange(60,200)  #heart_rate
			hr2=random.randrange(60,200)
			if diff % 1000 == 0:
				st1=random.randrange(0,3)
				st2=random.randrange(0,3)
				print '-------------------'+str(diff)+'-----------------------'
			data1=str(now)+","+str(u1)+","+str(st1)+","+str(hr1)
			data2=str(now)+","+str(u2)+","+str(st2)+","+str(hr2)
			producer.send('stream_test',data1)
			producer.send('stream_test',data2)
			print '*'
			if diff ==tp:
				rediscon.set('active',0)
				res=rediscon.get('active')
				diff=0		
		res=rediscon.get('active')

stream_generator()
	





