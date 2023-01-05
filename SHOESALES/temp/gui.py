from tkinter import *
from tkinter import messagebox
import tempfile
import datetime
import mysql.connector
import os
mydb=mysql.connector.connect(host="localhost",user="root",passwd="AsDev@321",database="sms1")
mycursor=mydb.cursor()
now=datetime.datetime.now()
odate=now.strftime("%y-%m-%d")
otime=now.strftime("%H:%M:%S")

def code_check(x):
    x>1

def insert_new(code,name,quantity,price):
       
    rpcode=code_check(code)
    if rpcode!=code:
        sqlf="insert into stock(pcode,pname,quantity,price)values(%s,%s,%s,%s)"
        s=code,name,quantity,price
        mycursor.execute(sqlf,s)
        messagebox.showinfo("New Stock","New stock added successfully")
        mydb.commit()
    else:
        messagebox.showwarning("New Stock","Already product exist in this code!!! Enter some other code")

def open_new_stock():
    top=Toplevel()
    top.title("New Stock Entry")
    top.geometry("600x600")

    ncode=StringVar()
    nname=StringVar()
    nquantity=StringVar()
    nprice=StringVar()
            
    F1=LabelFrame(top,text="New Stock Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
    F1.place(x=0,y=80,relwidth=1)

    code_lbl=Label(F1,text="Product Code:",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
    code_txt=Entry(F1,width=20,textvariable=ncode,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

    name_lbl=Label(F1,text="Product Name:",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=20,pady=5)
    name_txt=Entry(F1,width=20,textvariable=nname,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)

    quantity_lbl=Label(F1,text="Product Quantity",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=5,column=0,padx=20,pady=5)
    quantity_txt=Entry(F1,width=20,textvariable=nquantity,font="arial 15",bd=7,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)

    price_lbl=Label(F1,text="Product Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=7,column=0,padx=20,pady=5)
    price_txt=Entry(F1,width=20,textvariable=nprice,font="arial 15",bd=7,relief=SUNKEN).grid(row=7,column=1,pady=5,padx=10)

    insert=Button(F1,text="Insert",command=lambda:insert_new(int(ncode.get()),nname.get(),int(nquantity.get()),int(nprice.get())),bg="cadetblue",fg="white",pady=15,width=11,font="arial 10 bold").grid(row=12,column=0,padx=5,pady=5)

def update_stock(ucode,uquantity):
    rpcode=code_check(ucode)
    if rpcode==ucode:
        us="update stock set quantity=quantity+%s where pcode=%s"
        inp=(uquantity,ucode)
        mycursor.execute(us,inp)
        mydb.commit()
        messagebox.showinfo("Update Stock","Stock updated successfully")
    else:
        messagebox.showwarning("Update Stock","Check the product code")
        
def open_update_stock():
    top=Toplevel()
    top.title("Update Stock")
    top.geometry("600x600")

    ncode=StringVar()
    nquantity=StringVar()
                
    F1=LabelFrame(top,text="Update Stock Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
    F1.place(x=0,y=80,relwidth=1)

    code_lbl=Label(F1,text="Product Code:",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
    code_txt=Entry(F1,width=20,textvariable=ncode,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

    quantity_lbl=Label(F1,text="Product Quantity",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=20,pady=5)
    quantity_txt=Entry(F1,width=20,textvariable=nquantity,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)

    update=Button(F1,text="Update",command=lambda:update_stock(int(ncode.get()),int(nquantity.get())),bg="cadetblue",fg="white",pady=15,width=11,font="arial 10 bold").grid(row=5,column=0,padx=5,pady=5)

def update_price(ucode,uprice):
    rpcode=code_check(ucode)
    if rpcode==ucode:
        up="update stock set price=%s where pcode=%s"
        inp=(uprice,ucode)
        mycursor.execute(up,inp)
        mydb.commit()
        messagebox.showinfo("Update Price","Product price updated successfully")
    else:
        messagebox.showwarning("Update Price","Check the product code")

def open_update_price():
    top=Toplevel()
    top.title("Update price")
    top.geometry("600x600")

    ncode=StringVar()
    nprice=StringVar()
                
    F1=LabelFrame(top,text="Update Stock Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
    F1.place(x=0,y=80,relwidth=1)

    code_lbl=Label(F1,text="Product Code:",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
    code_txt=Entry(F1,width=20,textvariable=ncode,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

    price_lbl=Label(F1,text="Product Price:",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=20,pady=5)
    price_txt=Entry(F1,width=20,textvariable=nprice,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)

    update=Button(F1,text="Update",command=lambda:update_price(int(ncode.get()),int(nprice.get())),bg="cadetblue",fg="white",pady=15,width=11,font="arial 10 bold").grid(row=5,column=0,padx=5,pady=5)

def delete_stock(dcode):
    rpcode=code_check(dcode)
    if rpcode==dcode:
        d="delete from stock where pcode=%s"
        mycursor.execute(d,(dcode,))
        mydb.commit()
        messagebox.showinfo("Delete Stock","Product deleted successfully")
    else:
        messagebox.showwarning("Delete Stock","Check the product code")

def open_delete_stock():
    top=Toplevel()
    top.title("Delete Stock")
    top.geometry("600x600")

    ncode=StringVar()
                    
    F1=LabelFrame(top,text="Update Stock Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
    F1.place(x=0,y=80,relwidth=1)

    code_lbl=Label(F1,text="Product Code:",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
    code_txt=Entry(F1,width=20,textvariable=ncode,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

    delete=Button(F1,text="Delete",command=lambda:delete_stock(int(ncode.get())),bg="cadetblue",fg="white",pady=15,width=11,font="arial 10 bold").grid(row=5,column=0,padx=5,pady=5)

def next_entry():
    code.set("")
    quantity.set("")

def clear():
    cname.set("")
    cphone.set("")
    code.set("")
    quantity.set("")
    txtarea.delete("1.0",END)
def listpro():
    # a=input('Enter the product number :')
    mycursor.execute("select * from stock")
    dt=mycursor.fetchall()
    dt1=list(dt[0])
    # dt1=list(dt[0])
    # print("product name :",dt1[1])
    # print("cost per product:",dt1[2])
    # print("stock available:",dt1[3])
    # print(" Number items purchased :",dt1[4])
    txtarea.delete(1.0,END)
    # txtarea.insert(END,'    PRODUCT NAME \tNumber of Items\t  Cost of Items\n')
    txtarea.insert(END,f'\nBRAND NAME\t\t{dt1[1]}\t  {dt1[2]}')
    # txtarea.insert(END,' Items\tNumber of Items\t  Cost of Items\n')
    txtarea.insert(END,f'\nPRODUCT CODE\t\t{dt1[2]}\t  {dt1[2]}')
    txtarea.insert(END,f'\n\n\t\t{quantity.get()}\t  {cw.get()}')
    txtarea.insert(END,f'\n\nCUSTOMER NAME\t\t{cname.get()}\t  {cr.get()}')
    txtarea.insert(END,f'\n\nCUSTOMER PHONE NO\t\t{cphone.get()}\t  {cg.get()}')
    txtarea.insert(END, f"\n\n================================")
    # txtarea.insert(END,f'\nTotal Price\t\t{Total.get()}\t{total_cost.get()}')
    txtarea.insert(END, f"\n================================")

root=Tk()
root.title('Billing Manangement System')
root.geometry('1280x720')
bg_color='#2D9290'
title=Label(root,text=" SHOE Billing software",bd=12,bg=bg_color,fg="white",relief=GROOVE,font=("Times New Roman",30,"bold"),pady=2).pack(fill=X)

cname=StringVar()
cphone=StringVar()
code=StringVar()
quantity=StringVar()
Total=StringVar()
cb=StringVar()
cw=StringVar()
cr=StringVar()
cg=StringVar()
total_cost=StringVar()

def total():
    if code.get()==0 and quantity.get()==0:
        messagebox.showerror('Error','Please select number of quantity')
    else:
        b=Bread.get()
        w=Wine.get()
        r=Rice.get()
        g=Gal.get()

        t=float(b*10+w*1000+r*40+g*100)
        Total.set(b + w + r + g)
        total_cost.set('Rs ' + str(round(t, 2)))

        cb.set('Rs '+str(round(b * 10, 2)))
        cw.set('Rs '+str(round(w*1000,2)))
        cr.set('Rs '+str(round(r*40,2)))
        cg.set('Rs '+str(round(g*100,2)))

def receipt():
    txtarea.delete(1.0,END)
    txtarea.insert(END,' Items\tNumber of Items\t  Cost of Items\n')
    txtarea.insert(END,f'\nPRODUCT CODE\t\t{code.get()}\t  {cb.get()}')
    txtarea.insert(END,f'\n\n\t\t{quantity.get()}\t  {cw.get()}')
    txtarea.insert(END,f'\n\nCUSTOMER NAME\t\t{cname.get()}\t  {cr.get()}')
    txtarea.insert(END,f'\n\nCUSTOMER PHONE NO\t\t{cphone.get()}\t  {cg.get()}')
    txtarea.insert(END, f"\n\n================================")
    # txtarea.insert(END,f'\nTotal Price\t\t{Total.get()}\t{total_cost.get()}')
    txtarea.insert(END, f"\n================================")

F1=LabelFrame(root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=20,textvariable=cname,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

cphone_lbl=Label(F1,text="Customer Phoneno",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=20,textvariable=cphone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

F2=LabelFrame(root,text="SHOE Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
F2.place(x=5,y=170,width=600,height=360)

code_lbl=Label(F2,text="SHOE Code:",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
code_txt=Entry(F2,width=20,textvariable=code,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

quantity_lbl=Label(F2,text="SHOE Quantity",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=20,pady=5)
quantity_txt=Entry(F2,width=20,textvariable=quantity,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)

F3=Frame(root,bd=10,relief=GROOVE)
F3.place(x=620,y=170,width=650,height=360)
bill_title=Label(F3,text="Bill",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
txtarea=Text(F3,yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=txtarea.yview)
txtarea.pack(fill=BOTH,expand=1)

F4=LabelFrame(root,bd=10,relief=GROOVE,text="Stock Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
F4.place(x=0,y=535,relwidth=1,height=120)

stock_btn=Frame(F4,bd=7,relief=GROOVE)
stock_btn.place(x=0,width=685,height=105)

new_stock_entry=Button(stock_btn,text="New Stock Entry",command=open_new_stock,bg="cadetblue",fg="white",pady=15,width=16,font="arial 10 bold").grid(row=0,column=0,padx=5,pady=5)
update_sto=Button(stock_btn,text="Update Stock",command=open_update_stock,bg="cadetblue",fg="white",pady=15,width=15,font="arial 10 bold").grid(row=0,column=1,padx=5,pady=5)
update_pri=Button(stock_btn,text="Update Price",command=open_update_price,bg="cadetblue",fg="white",pady=15,width=15,font="arial 10 bold").grid(row=0,column=2,padx=5,pady=5)
delete_sto=Button(stock_btn,text="Delete Stock",command=open_delete_stock,bg="cadetblue",fg="white",pady=15,width=15,font="arial 10 bold").grid(row=0,column=3,padx=5,pady=5)


btn_f=Frame(F4,bd=7,relief=GROOVE)
btn_f.place(x=640,width=685,height=105)

'''bill_date=billno_date(odate)
bill_time=billno_time(otime)
bill_no=str(bill_date)+str(bill_time)'''

add_bill=Button(btn_f,text="Add To Bill",command=listpro,bg="cadetblue",fg="white",pady=15,width=11,font="arial 10 bold").grid(row=0,column=0,padx=5,pady=5)
remove_bill=Button(btn_f,text="Remove from Bill",bg="cadetblue",fg="white",pady=15,width=15,font="arial 10 bold").grid(row=0,column=1,padx=5,pady=5)
next_entry=Button(btn_f,text="Next Entry",bg="cadetblue",fg="white",pady=15,width=11,font="arial 10 bold").grid(row=0,column=2,padx=5,pady=5)
gen_bill=Button(btn_f,text="Generate Bill",command=listpro,bg="cadetblue",fg="white",pady=15,width=11,font="arial 10 bold").grid(row=0,column=3,padx=5,pady=5)
clear=Button(btn_f,text="Clear",bg="cadetblue",fg="white",pady=15,width=11,font="arial 10 bold").grid(row=0,column=4,padx=5,pady=5)

root.mainloop()