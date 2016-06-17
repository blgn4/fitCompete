from app import app
import redis

rediscon=redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')

@app.route('/index')
def index():
	return 'Fit Compete Analytics'




