import redis
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)
today_date="competetors"+time.strftime("%d-%m-%Y")
uid=100000
for i in (1,100):
	u1=uid+i
	u2=2*uid+i
	comp=str(u1)+","+str(u2)
	r.lpush(today_date,comp)
