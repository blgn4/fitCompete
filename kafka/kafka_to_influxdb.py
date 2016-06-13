import json
from kafka import KafkaConsumer
from influxdb import InfluxDBClient
from collections import OrderedDict

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.subscribe(['influxdb3'])

for msg in consumer:
        data=msg.value
        d=data.split(",")

        data1=[{"measurement":"fitbit_data" , "tags":{"user_id":int(d[0][1:]),"bmi":+int(d[1]),"fat":int(d[2]),"steps":int(d[3]),"floors":int(d[4]),"calories":int(d[5])},"fields":{"speed":int(d[7]),"calories_rate":int(d[6]),"heart_rate":int(d[6]),"total_time":int(d[9]),"date":d[10][:-1] }}]

        client=InfluxDBClient('localhost',8086,'root','root','niha_db_ex')
        client.write_points(data1)



