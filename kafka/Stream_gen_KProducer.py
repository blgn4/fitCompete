import time
from kafka import KafkaProducer
import random
from time import sleep
import sys
import datetime

producer = KafkaProducer(bootstrap_servers=["52.41.140.111:9092","52.41.90.5:9092","52.41.120.152:9092"])

def generate_ex_profile(usr,date):
	now=datetime.datetime.now()-datetime.timedelta(hours=7)
	hr=random.randrange(60,200)
	speed=random.randrange(2,6)
	cal_out_rate=random.randrange(6,10)
	data1=str(now)+","+str(usr)+","+str(hr)+","+str(speed)+","+str(cal_out_rate)+","+date
	producer.send('user_timeseries',data1)
	print str(usr)

while (1):
	now_t= datetime.datetime.now()-datetime.timedelta(hours=7)
	now=int(now_t.strftime('%H'))
	date=now_t.strftime("%d-%m-%Y")
	if now >= 4 and now < 11:
		usrr = random.randrange(1,400001)
		generate_ex_profile(usrr,date)
	elif now >=11 and now < 15:
		sleep(2)
		usrr = random.randrange(400001,500001)
		generate_ex_profile(usrr,date)
	elif now >=15 and now < 20:
		usrr = random.randrange(500001,900001)
		generate_ex_profile(usrr,date)
	elif now >=20 and now < 23:
		sleep(2)
		usrr = random.randrange(900001,1000001)
		generate_ex_profile(usrr,date)
	else:
		sleep(1)











