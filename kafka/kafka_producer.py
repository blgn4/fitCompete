from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def send_data(topic,data):
	producer.send(topic,data)

def generate_data():

	start_time=int(round(time.time()*1000))
	diff=0

	date=time.strftime("%d-%m-%Y")

	tot_time=random.randrange(900000,1800000,1)	

	us1=10000001
	us2=10000002

	
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

		d1={}
		d1['user_id']=us1
		d1['bmi']=bmi1
		d1['fat']=fat_range1
		d1['steps']=steps1
		d1['floors']=floors1
		d1['calories']=cal_in1
		d1['calories_rate']=cal_out_rate1
		d1['speed']=speed1
		d1['heart_rate']=hr1
		d1['total_workout_time']=tot_time
		d1['date']=date
		json_data1=json.dumps(d1)
		send_data('influxdb',json_data1)

		d2={}
		d2['user_id']=us2
		d2['bmi']=bmi2
		d2['fat']=fat_range2
		d2['steps']=steps2
		d2['floors']=floors2
		d2['calories']=cal_in2
		d2['calories_rate']=cal_out_rate2
		d2['speed']=speed2
		d2['heart_rate']=hr2
		d2['total_workout_time']=tot_time
		d2['date']=date
		json_data2=json.dumps(d2)
		send_data('influxdb1',json_data2)

		diff=int(round(time.time()*1000))-start_time

generate_data()








