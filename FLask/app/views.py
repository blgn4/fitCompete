from app import app
import redis
from flask import jsonify
from flask import render_template
from flask import request


def redis_counts(key_pattern):
	leng=0
	rediscon=redis.StrictRedis(host='localhost', port=6379, db=0,password='')
	keys=rediscon.keys(pattern=key_pattern)
	for key in keys:
		leng+=rediscon.llen(key)
	return leng


@app.route('/')
def index():
	return render_template("index.html", title='Fit Compete Profile')

@app.route('/user_profile', methods=['POST'])
def my_form_post():
    user_id = request.form['text']
    key = 'user:'+user_id
    rediscon=redis.StrictRedis(host='ec2-52-40-47-83.us-west-2.compute.amazonaws.com', port=6379, db=0,password='')
    res= rediscon.lrange(key,0,-1)
    return render_template('user_profile.html', user_id=user_id,bmi=res[0],calories=res[1],cr=res[2],fat=res[3],floors=res[4],hr=res[5],period=res[6],speed=res[7],steps=res[8] )

@app.route('/_obtain_users')
def obtain_users():
	user_id=request.args.get('user_id')
	bmi = request.args.get('bmi')
	cal= request.args.get('cal')
	cr = request.args.get('cr')
	fat = request.args.get('fat')
  	floors = request.args.get('floors')
  	hr = request.args.get('hr')
  	period = request.args.get('period')
  	speed = request.args.get('speed')
  	steps = request.args.get('steps')
  	key = bmi+cal+cr+fat+floors+hr+speed+steps+period
  	print key
  	rediscon=redis.StrictRedis(host='ec2-52-40-47-83.us-west-2.compute.amazonaws.com', port=6379, db=0,password='')
  	user_list=rediscon.lrange(key,0,500)
  	print user_list
  	res=user_list	
  	# if len(user_list) == 0: #or (len(user_list) == 1 and user_list[0]==user_id):
  	# 	res='No users match'
  	# else:
  	# 	res=user_list
  	return jsonify(result=res)

@app.route('/_start_competetion')
def stream_gen():
	rediscon=redis.StrictRedis(host='ec2-52-40-47-83.us-west-2.compute.amazonaws.com', port=6379, db=0,password='')
	res1=rediscon.blpop('stream',timeout=60)
	res2=rediscon.blpop('stream',timeout=60)
	res=[]
	res.append(res1)
	res.append(res2)
	print res
	return jsonify(result=res)


