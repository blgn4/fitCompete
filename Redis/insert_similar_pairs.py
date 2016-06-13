import redis
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)
today_date="competetors"
uid=1000000
for i in range(1,100000):
	u1=uid+i
	i+=1
	u2=uid+i
	print(str(u1))
	comp=str(u1)+","+str(u2)
	r.lpush(today_date,comp)
