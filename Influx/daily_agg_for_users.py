def generate_user_profiles():
	client=InfluxDBClient('localhost',8086,'root','root','niha')
	query='select user_id,last(date) from fitbit_data group by  user_id'
	result = client.query(query)
	print result
