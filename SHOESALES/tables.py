import mysql.connector as sql
conn= sql.connect(host='localhost', user = 'root', password ='AsDev@321')
c1=conn.cursor()
c1.execute("create database sms")
c1.execute('use sms')
c1.execute("create table stock (product_no int(10) primary key,product_name varchar(30),cost_per_product int(10),stock int(10),purchased int(10) );")
c1.execute("create table user(username varchar(255),passwd varchar(255));")
conn.commit()
