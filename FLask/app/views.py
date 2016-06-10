from app import app
import redis

rediscon=redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')

@app.route('/index')
def index():
	elements=rediscon.lrange("competetors10-06-2016",0,-1)
	return '\n'.join(elements)

