import redis
import thread
import time
from kafka import KafkaProducer
import random
import threading

producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))


class userThreads (threading.Thread):
    def __init__(self,counter, user_1,user_2):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = str(user_1)+str(user_2)
    def run(self):
        print "Starting " + self.name
        generate_data(user_1, user_2)
        print "Exiting " + self.name

def obtain_users_from_redis():
	print hello
	r = redis.StrictRedis(host='ec2-52-10-235-49.us-west-2.compute.amazonaws.com', port=6379, db=0)
	key="competetors"
	count=1
	while r.llen(key)!=0:
		user_pair=r.lpop(key)
		print(user_pair)
		user=user_pair.split(',')
		sleep(1)
		thread1=userThreads(count,user[0],user[1])
		thread1.start()
		count=count+1
		
		

def generate_data(us1,us2):

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
		sleep(1)
		hr1=random.randrange(60,200,1)
		hr2=random.randrange(60,200,1)

		speed1=random.randrange(2,6)
		speed2=random.randrange(2,6)

		cal_out_rate1=random.randrange(6,10)
		cal_out_rate2=random.randrange(6,10)

		data1=str(us1)+","+str(bmi1)+","+str(fat_range1)+","+str(steps1)+","+str(floors1)+","+str(cal_in1)+","+str(cal_out_rate1)+","+str(speed1)+","+str(hr1)+","+str(tot_time)+","+date
		#send_data('influx',data1)

		data2=str(us2)+","+str(bmi2)+","+str(fat_range2)+","+str(steps2)+","+str(floors2)+","+str(cal_in2)+","+str(cal_out_rate2)+","+str(speed2)+","+str(hr2)+","+str(tot_time)+","+date
		#send_data('influx',data2)

		diff=int(round(time.time()*1000))-start_time

def send_data(topic,data):
	producer.send(topic,data)

obtain_users_from_redis()




