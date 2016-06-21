from pyspark import SparkContext, SparkConf
from influxdb import InfluxDBClient
import random
import time

# appName='Similarity_APP'
# master='spark://ec2-52-40-200-26.us-west-2.compute.amazonaws.com:7077'
# conf = SparkConf().setAppName(appName).setMaster(master)
# sc = SparkContext(conf=conf)
client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')


def form_tuples(s):
	strg=s['values'][0]
	return (strg[1],strg[2])

def write_into_influx(s):
	for i in s:
		print i
		que = "select mean(speed),mean(calories_rate),mean(heart_rate) from week3_try1 where user_id='"+i[0]+"' and date='"+i[1]+"' group by user_id"
		start_time= time.time()
		res = client.query(que)
		print("--- %s seconds ---" % (time.time() - start_time))
		res1= res.raw
		series=res1['series'][0]
		vals=series['values'][0]
		tags=series['tags']
		user_id=tags['user_id']
		speed=vals[1]
		calories_rate=vals[1]
		heart_rate=vals[2]

		bmi=random.randrange(18,35)
		fat=random.randrange(15,25)
		steps=random.randrange(1000,10000)
		floors=random.randrange(0,25)
		calories=random.randrange(1500,3000)
		data2=[{"measurement":"week4_final1","tags":{"user_id":user_id},"fields":{"bmi":int(bmi),"fat":int(fat),"steps":int(steps),"floors":int(floors), "calories":int(calories), "speed":int(float(speed)), "calories_rate":int(float(calories_rate)),"heart_rate":int(float(heart_rate))}}]
		client.write_points(data2)

		
		




query='select user_id,last(date) from week3_try1 group by  user_id'
result = client.query(query)
res=result.raw
count =0
serie=[]
series=res['series']
serie.append(series)
start_time=time.time()
for ser in serie:
	count +=1
	strg=ser['values'][0]
	que = "select mean(speed),mean(calories_rate),mean(heart_rate) from week3_try1 where user_id='"+strg[1]+"' and date='"+strg[2]+"' group by user_id"
	res = client.query(que)
	res1= res.raw
	series=res1['series'][0]
	vals=series['values'][0]
	tags=series['tags']
	user_id=tags['user_id']
	speed=vals[1]
	calories_rate=vals[1]
	heart_rate=vals[2]

	bmi=random.randrange(18,35)
	fat=random.randrange(15,25)
	steps=random.randrange(1000,10000)
	floors=random.randrange(0,25)
	calories=random.randrange(1500,3000)
	data2=[{"measurement":"week4_final1","tags":{"user_id":user_id},"fields":{"bmi":int(bmi),"fat":int(fat),"steps":int(steps),"floors":int(floors), "calories":int(calories), "speed":int(float(speed)), "calories_rate":int(float(calories_rate)),"heart_rate":int(float(heart_rate))}}]
	client.write_points(data2)

print("--- %s seconds ---" % (time.time() - start_time))



# raw_data=sc.parallelize(series)

# user_data=raw_data.map(form_tuples)

# user_data.foreachPartition(write_into_influx)

