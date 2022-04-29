import mysql.connector as d
con=d.connect(host='localhost',user='root',password='0000',database='employee')
cursor=con.cursor()
query="select * from information"
cursor.execute(query)
#fetchone
data1=cursor.fetchone()
print(data1)
#fetchmany
#data2=cursor.fetchmany(3)
#print(data2)
#fetchall
#data3=cursor.fetchall()
#print(data3)