import json
from kafka import KafkaConsumer
from influxdb import InfluxDBClient

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.subscribe(['influxdb2'])

for msg in consumer:
	data=msg.value
	d=data.split(",")
	data={}
	fields={}
	fields['speed']=int(d[7])
	fields['date']=d[10][:-1]
	fields['calories_rate']=int(d[6])
	fields['heart_rate']=int(d[8])
	fields['total_time']=int(d[9])
	data['fields']=fields
	tags={}
	tags['user_id']=int(d[0][1:])
	tags['bmi']=int(d[1])
	tags['fat']=int(d[2])
	tags['steps']=int(d[3])
	tags['floors']=int(d[4])
	tags['calories']=int(d[5])
	data['tags']=tags
	data['measurement']='fitbit_data'

	print(data)


client=InfluxDBClient('localhost',8086,'root','root','niha_db_ex')
client.write_points(json_data)



