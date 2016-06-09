import json
from kafka import KafkaConsumer
from influxdb import InfluxDBClient

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.subscribe(['influxdb2'])

for msg in consumer:
	print msg


'''
data={}
data['measurement']='fitbit_data'
tags={}
tags['user_id']=user_id
tags['bmi']=bmi
tags['fat']=fat
tags['steps']=steps
tags['floors']=floors
tags['calories']=calories
json_tags=json.dumps(tags)
data['tags']=json_tags
fields={}
fields['speed']=speed
fields['date']=date
fields['calories_rate']=calories_rate
fields['heart_rate']=heart_rate
fields['total_time']=tot_time
json_fields=json.dump(fields)
data['fields']=json_fields
json_data=json.dump(data)


client=InfluxDBClient('localhost',8086,'root','root','niha_db_ex')
client.write_points(json_data)
'''


