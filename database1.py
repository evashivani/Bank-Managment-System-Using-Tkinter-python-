import mysql.connector as c
con=c.connect(host='localhost',user='root',password='0000',database='employee')
#checking coonection is true or false
if con.is_connected():
    print('successfully connected!!')
else:
    print('not connected!!')
#creating cursor(IT is an object which help to execute query and fetch record from db)
cursor=con.cursor()
while True: # code runs infinite time until we stop it manually

    name=input('Enter the name')
    age=int(input('Enter the age'))
    salary=int(input('Enter the salary'))
    query="insert into information values('{}',{},{})".format(name,age,salary)


    #update database
    query1="update information set (name='{}' where age={})".format(name,age)
    cursor.execute(query)
    con.commit()  # for closing the connection
    print('Data entered successfully')
    choice = input('Enter the choice\n:press 1 for add more data \npress 2 for exit')

    if choice == '2':
        break;