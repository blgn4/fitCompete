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

	tot_time=random.randrange(900000,1800000,1)	

	us1=10000001
	us2=10000002

	hr1=random.randrange(60,200,1)
	hr2=random.randrange(60,200,1)

	while diff < tot_time:
		d1={}
		time_stamp=int(round(time.time()*1000))
		d1['timestamp']=time_stamp
		d1['heart_rate']=hr1
		json_data1=json.dumps(d1)
		send_data('influxdb',json_data1)

		d2={}
		d2['timestamp']=time_stamp
		d2['heart_rate']=hr2
		json_data2=json.dumps(d2)
		send_data('influxdb',json_data2)

generate_data()








