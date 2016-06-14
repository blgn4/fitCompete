from influxdb import InfluxDBClient

def generate_user_profiles():
	user_date={}
	client=InfluxDBClient('localhost',8086,'root','root','niha')
	query='select user_id,last(date) from fitbit_data group by  user_id'
	result = client.query(query)
	for x in result:
		user_date[x[0]['user_id']] = x[0]['last']
	for key, value in user_date.iteritems():
		que = "select mean(speed),mean(calories_rate),mean(heart_rate) from fitbit_data where user_id='"+str(key)+"' and date='"+value +"' group by user_id,bmi,fat,steps,floors,calories,total_time,date"
		res = client.query(que)
		res1= res.raw
		series=res1['series'][0]
		vals=series['values'][0]
		tags=series['tags']
		user_id=tags['user_id']
		total_time=tags['total_time']
		bmi=tags['bmi']
		fat=tags['fat']
		steps=tags['steps']
		floors=tags['floors']
		calories=tags['calories']
		speed=vals[1]
		calories_rate=vals[1]
		heart_rate=vals[2]
		data2=[{"measurement":"final_data1","tags":{"user_id":user_id},"fields":{"bmi":int(bmi),"fat":int(fat),"steps":int(steps),"floors":int(floors), "calories":int(calories), "speed":int(float(speed)), "calories_rate":int(float(calories_rate)),"heart_rate":int(float(heart_rate))}}]
		print data2
		client.write_point(data2)
		


generate_user_profiles()
