from pyspark import SparkContext, SparkConf
from influxdb import InfluxDBClient

def get_data_from_influx():
	client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')
	query='select * from final_data1'
	result=client.query(query)
	res=result.raw
	series=res['series'][0]
	vals=series['values']
	str2=[]
	count=0
	for val in vals:
				
		bmi=val[1]
		if bmi <24:
			str1+='L'
		elif bmi>=24 and bmi<30:
			str1+='M'
		else:
			str1+='H'
		
		calories=val[2]
		if calories < 2000:
			str1+='L'
		elif calories >= 2000 and calories <=2500:
			str1+='M'
		else:
			str1+='H'
		
		calories_rate=val[3]
		if calories_rate < 8:
			str1+='L'
		elif calories_rate >= 8 and calories_rate <=9:
			str1+='M'
		else:
			str1+='H'
		fat=val[4]
		if fat < 18:
			str1+='L'
		elif fat >= 18 and calories_rate <=21:
			str1+='M'
		else:
			str1+='H'
		floors=val[5]
		if floors < 8:
			str1+='L'
		elif floors >=8 and floors <= 16:
			str1+='M'
		else:
			str1+='H'
		heart_rate=val[6]
		if heart_rate < 107:
			str1+='L'
		elif heart_rate>=107 and heart_rate <= 153:
			str1+='M'
		else:
			str1+='H'
		speed=val[7]
		if speed < 4:
			str1+='L'
		elif speed >=4 and speed <5:
			str1+='M'
		else:
			str1+='H'
		steps=val[8]
		if steps <3000:
			str1+='L'
		elif steps >= 3000 and steps <= 6000:
			str1+='M'
		else:
			str1+='H'
		user_id=val[9]
		str1+=','
		str1+=user_id
		str2[count]=str1
		count +=1
	return str2

appName='Similarity_APP'
master='spark://ec2-52-40-200-26.us-west-2.compute.amazonaws.com:7077'
conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)

list_1 = get_data_from_influx()
distData = sc.parallelize(data)

