import mysql.connector as sql
conn= sql.connect(host='localhost', user = 'root', password ='AsDev@321',database ='sms')
c1=conn.cursor()
c1.execute('select product_no,product_name,cost_per_product,stock,purchased  from stock;')
peee=c1.fetchall()
peee1=list(peee)
print('''PRODUCT  PRODUCT NAME NO  COST PER PRODUCT STOCK PURCHASED QUANTITY''')                     
      
for i in range(0,int(len(peee))):
                print(peee[i] )
