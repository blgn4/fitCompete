from kafka import KafkaConsumer
from influxdb import InfluxDBClient

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.subscribe(['influxdb'])

for msg in consumer:
	user_id=msg['user_id']
	bmi=msg['bmi']
	fat=msg['fat']
	steps=msg['steps']
	floors=msg['floors']
	calories=msg['calories']
	calories_rate=msg['calories_rate']
	speed=msg['speed']
	heart_rate=msg['heart_rate']
	tot_time=msg['total_workout_time']
	date=msg['date']


json_data={"measurement":"fitbit_data","tags":{"user_id":user_id,"bmi":bmi,"fat":fat,"steps":steps,"floors":floors,"calories":calories},"fields":{"speed":speed,"date"=date,"calories_rate":calories_rate,"heart_rate":heart_rate,"total_time":tot_time}}

client=InfluxDBClient('localhost',8086,'root','root','niha_db_ex')
client.write_points(json_data)



