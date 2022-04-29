import mysql.connector as c
con=c.connect(host='localhost',user='root',password='0000',database='employee')
#checking coonection is true or false
if con.is_connected():
    print('successfully connected!!')
else:
    print('not connected!!')
#creating cursor(IT is an object which help to execute query and fetch record from db)
cursor=con.cursor()

name=input('Enter the name')
age=int(input('Enter the age'))
#update database
query1="update information set name='{}' where age={}".format(name,age)
cursor.execute(query1)
con.commit()  # for closing the connection
