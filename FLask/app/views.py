from app import app
import redis
import jsonify
from flask import render_template




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
	return render_template("index.html", title='Fit Compete Profile')

@app.route('/index', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

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





