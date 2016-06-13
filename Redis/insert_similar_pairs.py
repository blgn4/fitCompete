import redis
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)
key="competetors"
uid=1000000
i=1
while i<=60000:
	u1=uid+i
	i=i+1
	u2=uid+i
	i=i+1
	print(str(u1))
	comp=str(u1)+","+str(u2)
	r.lpush(key,comp)
