from pyspark import SparkContext, SparkConf
from influxdb import InfluxDBClient

def get_data_from_influx():
	client=InfluxDBClient('ec2-52-10-176-111.us-west-2.compute.amazonaws.com',8086,'root','root','niha')
	query='select * from final_data1'
	result=client.query(query)
	res=result.raw
	vals=res['series']['values']
	for val in vals:
		print val

get_data_from_influx()

