import mysql.connector as sql
import datetime
d_day=datetime.date.today()
d_time=datetime.datetime.now()
conn= sql.connect(host='localhost', user = 'root', password ='AsDev@321',database ='sms')
c1=conn.cursor()
print("\nDEX STORES SHOE SALES MANAGEMENT SYSTEM")
print(d_day.day,"/",d_day.month,"/",d_day.year,"    ",d_time.hour,":",d_time.minute,)
chpasswd='d'
while 5>1:
                print("\n1.LOGIN")
                print("2.REGISTER")
                print("3.VEIW ALL USERS")
                print("4.EXIT")
                choice=int(input('\nENTER THE CHOICE:'))
                print("============================================================================")
                if choice == 1:
                                us=input('USERNAME:')
                                ps=input('PASSWORD:')
                                c1.execute("select * from user where username = '{}' and passwd = '{}'".format(us , ps))
                                
                                data = c1.fetchall()
                                
                                if any(data) :
                                                import main
                                
                                else:
                                                print('''..SORRY..
WRONG.......USERNAME OR PASSWORD''')

                elif choice == 2:
                                print("===========================================================================================")
                                li=input('ENTER THE NEW USER ID:')
                                while 8>1:
                                                li2=input('ENTER YOUR PASSWORD:')
                                                li3=input('ENTER YOUR PASSWORD AGAIN(to confirm):')
                                                if li2== li3:
                                                                c1.execute("insert into user values("+'"'+li+'",'+'"'+li3+'")')
                                                                print("ID has been successfully created:")
                                                                conn.commit()
                                                                break
                elif choice ==3:
                                c1.execute("select username from user")
                                data = c1.fetchall()
                                for row in data : print(row)
                elif choice == 4:
                                print(".......................LOGGING...........OUT................")
                                break
                                        
                else:
                                print('please enter the right option')
