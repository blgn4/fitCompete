from influxdb imprt InfluxDBClient

client=InfluxDBClient('localhost',8086,'niha','niha',f_data)
print 'create database'
client.create_database('py_ex_db')