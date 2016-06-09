import json
from kafka import KafkaConsumer
from influxdb import InfluxDBClient

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.subscribe(['influxdb2'])

for msg in consumer:
	data=msg.value
	d=data.split(",")
	data={}
	data['measurement']='fitbit_data'
	tags={}
	tags['user_id']=d[0]
	tags['bmi']=d[1]
	tags['fat']=d[2]
	tags['steps']=d[3]
	tags['floors']=d[4]
	tags['calories']=d[5]
	data['tags']=tags
	fields={}
	fields['speed']=d[7]
	fields['date']=d[9]
	fields['calories_rate']=d[6]
	fields['heart_rate']=d[8]
	fields['total_time']=d[10]
	data['fields']=fields

	print(data)

'''
client=InfluxDBClient('localhost',8086,'root','root','niha_db_ex')
client.write_points(json_data)
'''


