import mysql.connector as d
con=d.connect(host='localhost',user='root',password='0000',database='employee')
cursor=con.cursor()
age=int(input('Enter the age'))
query="delete from information where age={}".format(age)
#if cursor.rowcount > 0:
    #print('data deleted successfully')
#else:
    #print("invalid input")
cursor.execute(query)
con.commit()