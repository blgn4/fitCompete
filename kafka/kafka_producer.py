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

		data1=us1+","+bmi1+","+fat_range1+","+steps1+","+floors1+","+cal_in1+","+cal_out_rate1+","+speed1+","+hr1+","+tot_time+","+date
		send_data('influxdb2',data1)

		data2=us2+","+bmi2+","+fat_range2+","+steps2+","+floors2+","+cal_in2+","+cal_out_rate2+","+speed2+","+hr2+","+tot_time+","+date
		send_data('influxdb2',data2)

		diff=int(round(time.time()*1000))-start_time

generate_data()








