from app import app
import redis
import jsonify




def redis_counts(key_pattern):
	leng=0
	rediscon=redis.StrictRedis(host='localhost', port=6379, db=0,password='')
	keys=rediscon.keys(pattern=key_pattern)
	for key in keys:
		leng+=rediscon.llen(key)
	return leng


@app.route('/')

@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/<feature>')
def get_counts_for_feature(feature):
	if feature=='bmi':
		low=redis_counts('L???????')
		medium=redis_counts('M???????')
		high=redis_counts('H???????')
		ress=[{"low":low,"medium":medium,"high":high}]
		return jsonify(result=ress)

	elif feature=='calories':
		low=redis_counts('?L??????')
		medium=redis_counts('?M??????')
		high=redis_counts('?H??????')
		ress=[{"low":low,"medium":medium,"high":high}]
		return jsonify(result=ress)
		
	elif feature=='calories_rate':
		low=redis_counts('??L?????')
		medium=redis_counts('??M?????')
		high=redis_counts('??H?????')
		ress=[{"low":low,"medium":medium,"high":high}]
		return jsonify(result=ress)
	elif feature=='fat':
		low=redis_counts('???L????')
		medium=redis_counts('???M????')
		high=redis_counts('???H????')
		ress=[{"low":low,"medium":medium,"high":high}]
		return jsonify(result=ress)
	elif feature=='floors':
		low=redis_counts('????L???')
		medium=redis_counts('????M???')
		high=redis_counts('????H???')
		ress=[{"low":low,"medium":medium,"high":high}]
		return jsonify(result=ress)
	elif feature=='heart_rate':
		low=redis_counts('?????L??')
		medium=redis_counts('?????M??')
		high=redis_counts('?????H??')
		ress=[{"low":low,"medium":medium,"high":high}]
		return jsonify(result=ress)
	elif feature=='speed':
		low=redis_counts('??????L?')
		medium=redis_counts('??????M?')
		high=redis_counts('??????H?')
		ress=[{"low":low,"medium":medium,"high":high}]
		return jsonify(result=ress)
	elif feature=='steps':
		low=redis_counts('???????L')
		medium=redis_counts('???????M')
		high=redis_counts('???????H')
		ress=[{"low":low,"medium":medium,"high":high}]
		return jsonify(result=ress)





