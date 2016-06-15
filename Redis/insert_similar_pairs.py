import redis
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)
key="timeperiod1"
uid=100000
i=1
while i<=30000:
	comp=uid+i
	r.lpush(key,comp)
	i=i+1
print i

key="timeperiod2"
while i<=45000:
	comp=uid+i
	r.lpush(key,comp)
	i=i+1
print i

key="timeperiod3"
while i<=75000:
	comp=uid+i
	r.lpush(key,comp)
	i=i+1
print i

key="timeperiod4"
while i<=90000:
	comp=uid+i
	r.lpush(key,comp)
	i=i+1
print i

key="timeperiod5"
while i<=99999:
	comp=uid+i
	r.lpush(key,comp)
	i=i+1
print i



