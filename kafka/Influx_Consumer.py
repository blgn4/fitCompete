from kafka import KafkaConsumer
from influxdb import InfluxDBClient
#all kafka brokers are added
consumer = KafkaConsumer('user_timeseries',bootstrap_servers=["52.41.140.111:9092","52.41.90.5:9092","52.41.120.152:9092"])

for msg in consumer:
        data=msg.value
        print data
        d=data.split(",")
        data1=[{"measurement":"fit_timeseries","tags":{"user_id":int(d[1])},"time":int(d[0]),"fields":{"heart_rate":int(d[1]),"speed":int(d[2]),"calories_rate":int(d[3]),"date":d[4]}}]
        client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')
        client.write_points(data1)



