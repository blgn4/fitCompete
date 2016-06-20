from pyspark import SparkContext, SparkConf
from influxdb import InfluxDBClient
import random

appName='Similarity_APP'
master='spark://ec2-52-40-200-26.us-west-2.compute.amazonaws.com:7077'
conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)
user_date={}
client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')
query='select user_id,last(date) from week3_try1 group by  user_id'
result = client.query(query)

# user_date_raw=sc.parallelize(result)
# user_date=user_date_raw.map()
count=0
for x in result:
	print count
	count+=1
	# user_date[x[0]['user_id']] = x[0]['last']
# print 'done obtaining user latest dates'
# for key, value in user_date.iteritems():
# 	que = "select mean(speed),mean(calories_rate),mean(heart_rate) from week3_try1 where user_id='"+str(key)+"' and date='"+value +"' group by user_id"
# 	res = client.query(que)
# 	res1= res.raw
# 	series=res1['series'][0]
# 	vals=series['values'][0]
# 	tags=series['tags']
# 	user_id=tags['user_id']
# 	speed=vals[1]
# 	calories_rate=vals[1]
# 	heart_rate=vals[2]

# 	bmi=random.randrange(18,35)
# 	fat=random.randrange(15,25)
# 	steps=random.randrange(1000,10000)
# 	floors=random.randrange(0,25)
# 	calories=random.randrange(1500,3000)
# 	data2=[{"measurement":"week3_final1","tags":{"user_id":user_id},"fields":{"bmi":int(bmi),"fat":int(fat),"steps":int(steps),"floors":int(floors), "calories":int(calories), "speed":int(float(speed)), "calories_rate":int(float(calories_rate)),"heart_rate":int(float(heart_rate))}}]
# 	client.write_points(data2)
# print 'done!!'
	


# generate_user_profiles()
