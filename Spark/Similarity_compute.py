from pyspark import SparkContext, SparkConf
from influxdb import InfluxDBClient

def get_data_from_influx():
	client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')
	query='select * from final_data1'
	result=client.query(query)
	res=result.raw
	series=res['series'][0]
	vals=series['values']
	for val in vals:
		str1=''
		
		bmi=vals[1]
		if bmi <24:
			str1+='L'
		else if bmi>=24 && bmi<30:
			str1+='M'
		else:
			str1+='H'
		
		calories=vals[2]
		if calories < 2000:
			str1+='L'
		else if calories >= 2000 && calories <=2500:
			str1+='M'
		else:
			str1+='H'
		
		calories_rate=vals[3]
		if calories_rate < 8:
			str1+='L'
		else if calories_rate >= 8 && calories_rate <=9:
			str1+='M'
		else:
			str1+='H'
		fat=vals[4]
		if fat < 18:
			str1+='L'
		else if fat >= 18 && calories_rate <=21:
			str1+='M'
		else:
			str1+='H'
		floors=vals[5]
		if floors < 8:
			str1+='L'
		else if floors >=8 && floors <= 16:
			str1+='M'
		else:
			str1+='H'
		heart_rate=vals[6]
		if heart_rate < 107:
			str1+='L'
		else if heart_rate>=107 && heart_rate <= 153:
			str1+='M'
		else:
			str1+='H'
		speed=vals[7]
		if speed < 4:
			str1+='L'
		else if speed >=4 && speed <5:
			str1+='M'
		else:
			str1+='H'
		steps=vals[8]
		if steps <3000:
			str1+='L'
		else if steps >= 3000 && steps <= 6000:
			str1+='M'
		else:
			str1+='H'
		user_id=vals[9]
		str1+=user_id
		print str1


get_data_from_influx()

