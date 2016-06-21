from influxdb import InfluxDBClient
import time


client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')

start_time=time.time()
que = "select mean(speed),mean(calories_rate),mean(heart_rate) from week3_try1  where date='16-06-2016' group by user_id"
res = client.query(que)
res1= res.raw
series=res1['series']
for val in series:
	vals=val['values'][0]
	tags=val['tags']
	user_id=tags['user_id']
	speed=vals[0]
	calories_rate=vals[1]
	heart_rate=vals[2]
	bmi=random.randrange(18,35)
	fat=random.randrange(15,25)
	steps=random.randrange(1000,10000)
	floors=random.randrange(0,25)
	calories=random.randrange(1500,3000)
print("--- %s seconds ---" % (time.time() - start_time))