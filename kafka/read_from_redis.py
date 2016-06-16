import redis
import time
from kafka import KafkaProducer
import random
from time import sleep
import sys
import datetime

producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
redis_client = redis.StrictRedis(host='ec2-52-10-235-49.us-west-2.compute.amazonaws.com', port=6379, db=0)


while (1):
	now = int(datetime.datetime.now().strftime('%H'))
	if now >= 4 and now < 11:
		usrr = random.randrange(1,10000)
		generate_ex_profile(usrr)
	elif now >=11 and now < 15:
		sleep(2)
		usrr = random.randrange(1,10000)
		generate_ex_profile(usrr)
	elif now >=15 and now < 20:
		usrr = random.randrange(1,10000)
		generate_ex_profile(usrr)
	elif now >=20 and now < 23:
		sleep(2)
		usrr = random.randrange(1,10000)
		generate_ex_profile(usrr)
	elif now >=23 and now <=24:
		sleep(10)
		usrr = random.randrange(1,10000)
		generate_ex_profile(usrr)
	else:
		sleep(14400)


def generate_ex_profile(usr):
	hr=random.randrange(60,200)
	speed=random.randrange(2,6)
	cal_out_rate=random.randrange(6,10)
	date=time.strftime("%d-%m-%Y")
	data1=str(usr)+","+str(hr)+","+str(speed)+","+str(cal_out_rate)+","+date
	send_data('influx',data1)


def send_data(topic,data):
	producer.send(topic,data)





