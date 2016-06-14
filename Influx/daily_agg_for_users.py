from influxdb import InfluxDBClient

def generate_user_profiles():
	user_date={}
	client=InfluxDBClient('localhost',8086,'root','root','niha')
	query='select user_id,last(date) from fitbit_data group by  user_id'
	result = client.query(query)
	for x in result:
		user_date[x[0]['user_id']] = x[0]['last']
	for key, value in d.iteritems():
		que = 'select mean(speed),mean(calories_rate),mean(heart_rate) from fitbit_data where user_id='+str(key)+'and date='+value +'group by user_id,bmi,fat,steps,floors,calories,total_time'
		res = client.query(query)
		print res

generate_user_profiles()
