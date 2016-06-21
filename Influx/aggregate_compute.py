from influxdb import InfluxDBClient
import time


client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')

start_time=time.time()
que = "select mean(speed),mean(calories_rate),mean(heart_rate) from week3_try1 group by user_id"
res = client.query(que)
res1= res.raw
print("--- %s seconds ---" % (time.time() - start_time))