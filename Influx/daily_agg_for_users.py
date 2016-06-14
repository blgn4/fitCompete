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
		print res
		
		'''
		user_id=key[1]['user_id']
		total_time=key[1]['total_time']
		bmi=key[1]['bmi']
		fat=key[1]['fat']
		steps=key[1]['steps']
		floors=key[1]['floors']
		calories=key[1]['calories']
		speed=val[0]['mean']
		calories_rate=val[0]['mean_1']
		heart_rate=val[0]['mean_2']
		data2={"measurement":"final_data1","tags":{"user_id":user_id},"fields":{"bmi":int(bmi),"fat":int(fat),"steps":int(steps),"floors":int(floors), "calories":int(calories), "speed":int(float(speed)), "calories_rate":int(float(calories_rate)),"heart_rate":int(float(heart_rate))}}
		client.write_point(data2)
		'''


generate_user_profiles()
