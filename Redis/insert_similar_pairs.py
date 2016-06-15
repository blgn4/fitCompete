import redis
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)
key="timeperiod1"
uid=100000
i=1
while i<=29999:
	u1=uid+i
	i=i+1
	u2=uid+i
	i=i+1
	comp=str(u1)+","+str(u2)
	r.lpush(key,comp)

print i
key="timeperiod2"
while i<=45001:
	u1=uid+i
	i=i+1
	u2=uid+i
	i=i+1
	comp=str(u1)+","+str(u2)
	r.lpush(key,comp)
print i
key="timeperiod3"
while i<=75001:
	u1=uid+i
	i=i+1
	u2=uid+i
	i=i+1
	comp=str(u1)+","+str(u2)
	r.lpush(key,comp)
print i
key="timeperiod4"
while i<=90001:
	u1=uid+i
	i=i+1
	u2=uid+i
	i=i+1
	comp=str(u1)+","+str(u2)
	r.lpush(key,comp)
print i
key="timeperiod5"
while i<=99999:
	u1=uid+i
	i=i+1
	u2=uid+i
	i=i+1
	comp=str(u1)+","+str(u2)
	r.lpush(key,comp)
print i



