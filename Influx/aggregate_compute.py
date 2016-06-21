from influxdb import InfluxDBClient
import time


client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')

start_time=time.time()
query='select user_id,last(date) from week3_try1 where time <= now() -1d group by  user_id '
result = client.query(query)
res=result.raw
count =0
series=res['series']
for val in series:
	i=val['values'][0]
	que = "select mean(speed),mean(calories_rate),mean(heart_rate) from week3_try1 where user_id='"+i[0]+"' and date='"+i[1]+"' group by user_id"
	res = client.query(que)
	res1= res.raw
print("--- %s seconds ---" % (time.time() - start_time))