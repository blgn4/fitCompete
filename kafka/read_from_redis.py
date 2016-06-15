import redis
import time
from kafka import KafkaProducer
import random
from time import sleep
import sys


import datetime

producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
redis_client = redis.StrictRedis(host='ec2-52-10-235-49.us-west-2.compute.amazonaws.com', port=6379, db=0)

def check_timings():
	key=''
	now = int(datetime.datetime.now().strftime('%H'))
	if now >= 5 and now < 11:
		key ='timeperiod1'
	elif now >=11 and now < 15:
		key='timeperiod2'
	elif now >=15 and now < 20:
		key = 'timeperiod3'
	elif now >=20 and now <23:
		key = 'timeperiod4'
	elif now >=23 and now <=24:
		key='timeperiod5'
	else:
		key='sleep'
	return key

key = check_timings()
while key != 'sleep':
	list_length=redis_client.llen(key)
	user_number=random.randrange(0,listlength+1)
	generate_ex_profile(user_number)
	key = check_timings()

if key == 'sleep':
	sys.exit()


def generate_ex_profile(usr):
	hr=random.randrange(60,200)
	speed=random.randrange(2,6)
	cal_out_rate=random.randrange(6,10)
	date=time.strftime("%d-%m-%Y")
	data1=str(usr)+","+str(hr)+","+str(speed)+","+str(cal_out_rate)+","+date
	send_data('influx',data1)


def send_data(topic,data):
	producer.send(topic,data)


'''
def obtain_users_from_redis():
	print('hello')
	r = redis.StrictRedis(host='ec2-52-10-235-49.us-west-2.compute.amazonaws.com', port=6379, db=0)
	key="competetors"
	count=1
	while r.llen(key)!=0:
		user_pair=r.lpop(key)
		user=user_pair.split(',')
		thread1=userThreads(count,user[0],user[1])
		thread1.start()
		generate_data(user[0],user[1])
		count=count+1
		sleep(900)
		
		

def generate_data(us1):


	start_time=int(round(time.time()*1000))
	diff=0

	date=time.strftime("%d-%m-%Y")

	tot_time=random.randrange(900000,1800000,1)	

	
	bmi1=random.randrange(18,35)
	bmi2=random.randrange(18,35)

	fat_range1=random.randrange(15,25)
	fat_range2=random.randrange(15,25)

	steps1=random.randrange(1000,10000)
	steps2=random.randrange(1000,10000)

	floors1=random.randrange(0,25)
	floors2=random.randrange(0,25)

	cal_in1=random.randrange(1500,3000)
	cal_in2=random.randrange(1500,3000)

	

	while diff < tot_time:
		hr1=random.randrange(60,200,1)
		hr2=random.randrange(60,200,1)

		speed1=random.randrange(2,6)
		speed2=random.randrange(2,6)

		cal_out_rate1=random.randrange(6,10)
		cal_out_rate2=random.randrange(6,10)

		data1=str(us1)+","+str(bmi1)+","+str(fat_range1)+","+str(steps1)+","+str(floors1)+","+str(cal_in1)+","+str(cal_out_rate1)+","+str(speed1)+","+str(hr1)+","+str(tot_time)+","+date
		print data1
		send_data('topic1',data1)

		data2=str(us2)+","+str(bmi2)+","+str(fat_range2)+","+str(steps2)+","+str(floors2)+","+str(cal_in2)+","+str(cal_out_rate2)+","+str(speed2)+","+str(hr2)+","+str(tot_time)+","+date
		send_data('topic1',data2)

		diff=int(round(time.time()*1000))-start_time



obtain_users_from_redis()
'''



