import json
from kafka import KafkaConsumer
from influxdb import InfluxDBClient
from collections import OrderedDict

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.subscribe(['week3_topic'])

for msg in consumer:
        data=msg.value
        d=data.split(",")
		data1=[{"measurement":"week3_try1","tags":{"user_id":int(d[0][1:])},"fields":{"heart_rate":int(d[1]),"speed":int(d[2]),"calories_rate":int(d[3]),"date":d[4][:-1]}}]
		print d[0][1:]
        client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')
        client.write_points(data1)



