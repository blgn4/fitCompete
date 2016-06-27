import time
from kafka import KafkaProducer
import random
from time import sleep
import sys
import datetime

def stream_generator():

	producer = KafkaProducer(bootstrap_servers=["52.41.140.111:9092","52.41.90.5:9092","52.41.120.152:9092"])

	tp=random.randrange(900000,1800001)
	st =  int(round(time.time() * 1000))
	diff=0
	while  diff <=tp:
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
			st2=random.ranrange(0,3)
			print '-------------------'+str(diff)+'-----------------------'
		data1=str(now)+","+str(u1)+","+str(st1)+","+str(hr1)
		data2=str(now)+","+str(u2)+","+str(st2)+","+str(hr2)
		producer.send('stream_test',data1)
		producer.send('stream_test',data2)
		print '*'





