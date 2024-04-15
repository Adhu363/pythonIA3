import tkinter.messagebox
from tkinter import *
import mysql.connector as sqlcon
import random as rd

con=sqlcon.connect(host="localhost",user="root",password="6363")#connection to mysql 
cur=con.cursor()
cur = con.cursor(buffered=True)
if (con):
    # Carry out normal procedure
    print ("Connection successful")
else:
    print ("Connection unsuccessful")
cur.execute("create database if not exists Carrent")
cur.execute("use Carrent")
cur.execute("create table if not exists booking"
            "("
            "idno varchar(12) primary key,"
            "name char(50),"
            "age char(3),"
            "gender char(1),"
            "phone varchar(10),"
            "bg varchar(3))")
cur.execute("create table if not exists booking_details"
            "("
            "idno varchar(12) primary key,"
            "doctor varchar(50),"
            "date varchar(20),"
            "time varchar(20),"
            "booking_no varchar(10))")

# Message for registration
def entry():
    global e1,e2,e3,e4,e5,e6
    p1=e1.get()
    p2=e2.get()
    p3=e3.get()
    p4=e4.get()
    p5=e5.get()
    p6=e6.get()

    query='insert into booking values("{}", "{}", "{}", "{}", "{}", "{}")'.format(p1,p2,p3,p4,p5,p6)
    con.commit()
    cur.execute(query)
    
        
    
    tkinter.messagebox.showinfo("DONE", "YOU HAVE BEEN REGISTERED")

# For registration 
def register():
    global e1,e2,e3,e4,e5,e6
    root1=Tk()
    label=Label(root1,text="REGISTER YOURSELF",font='arial 25 bold')
    label.pack()
    frame=Frame(root1,height=500,width=200)
    frame.pack()
    l1=Label(root1,text="AADHAR CARD NO.")
    l1.place(x=10,y=130)
    e1=tkinter.Entry(root1)
    e1.place(x=100,y=130)
    l2=Label(root1,text="NAME")
    l2.place(x=10,y=170)
    e2=tkinter.Entry(root1)
    e2.place(x=100,y=170)
    l3=Label(root1,text="AGE")
    l3.place(x=10,y=210)
    e3=tkinter.Entry(root1)
    e3.place(x=100,y=210)
    l4=Label(root1,text="GENDER M\F")
    l4.place(x=10,y=250)
    e4=tkinter.Entry(root1)
    e4.place(x=100,y=250)
    l5=Label(root1,text="PHONE")
    l5.place(x=10,y=290)
    e5=tkinter.Entry(root1)
    e5.place(x=100,y=290)
    l6=Label(root1,text="CITY")
    l6.place(x=10,y=330)
    e6=tkinter.Entry(root1)
    e6.place(x=100,y=330)
    b1=Button(root1,text="SUBMIT",command=entry)
    b1.place(x=150,y=370)
    
    
    root.resizable(False,False)
    root1.mainloop()

# Message for appointment
def apo_details():
    global x1,x2,h,p1,p2,p3,o,x4,x3
    p1=x2.get()
    p2=x3.get()
    p3=x4.get()
    if int(p1)==1:
        i=("Nissan Versa \nRent:- $250")
        j=("Toyota Corolla \nRent:- $250")
        k=("Honda Civic \nRent:- $300")
        q=(i,j,k)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)
        det=("Your booking is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nbooking:-',o)

        query='insert into booking_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("BOOKING DETAILS",det)
     
    elif int(p1)==2:
        i=("Suzuki Vitara \nRent:- $250")
        j=("Jeep Cherokee \nRent:- $350")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your booking is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nbooking no:-',o)
        query='insert into booking_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query) 
        tkinter.messagebox.showinfo("BOOKING DETAILS",det)
     
    elif int(p1)==3:
        i=("Volkswagen Polo \nRent:- $270")
        j=("Audi A3 \nRent:- $350")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your booking is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nbooking no:-',o)
        query='insert into booking_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query) 
        tkinter.messagebox.showinfo("BOOKING DETAILS",det)

    elif int(p1)==4:
        i=("Ford F150 \nRent:- $300")
        j=("Dodge Ram \nRent:- $370")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your booking is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nbooking no:-',o)
        query='insert into booking_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("BOOKING DETAILS",det)
    elif int(p1)==5:
        i=("Maserati Quattroporte \nRent:- $480")
        j=("Porsche 911 \nRent:- $550")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your booking is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nbooking no:-',o)
        query='insert into booking_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("BOOKING DETAILS",det)   
    elif int(p1)==6:
        i=("Dodge Grand Caravan \nRent:- 400")
        j=("Honda Odyssey \nRent:- 300")
        k=("Toyota Sienna \nRent:- 340")
        
        q=(i,j,k)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your booking is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nbooking no:-',o)
        query='insert into booking_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("BOOKING DETAILS",det)   
    else:
        tkinter.messagebox.showwarning('WRONG INPUT','PLEASE ENTER VALID VALUE')

# For appointment
def get_apoint():
    global x1,x2,x3,x4
    p1=x1.get()  
    cur.execute('select * from booking where idno=(%s)',(p1,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        root3=Tk()
        label=Label(root3,text="BOOKING",font='arial 25 bold')
        label.pack()
        frame=Frame(root3,height=500,width=300)
        frame.pack()
        if i[3]=='M' or i[3]=='m':
                x="Mr."
                name2=Label(root3,text=i[1])
                name2.place(x=140,y=80)
        else:
                x="Mrs\Ms."
                name2=Label(root3,text=i[1])
                name2.place(x=170,y=80)
        for i in dat:
            name=Label(root3,text='WELCOME')
            name.place(x=50,y=80)
            name1=Label(root3,text=x)
            name1.place(x=120,y=80)
            age=Label(root3,text='AGE:-')
            age.place(x=50,y=100)
            age1=Label(root3,text=i[2])
            age1.place(x=100,y=100)
            phone=Label(root3,text='PHONE:-')
            phone.place(x=50,y=120)
            phone1=Label(root3,text=i[4])
            phone1.place(x=100,y=120)
            bg=Label(root3,text='CITY:-')
            bg.place(x=50,y=140)
            bg1=Label(root3,text=i[5])
            bg1.place(x=150,y=140)


        L=Label(root3,text='TYPE')
        L.place(x=50,y=220)
        L1=Label(root3,text="1.Sedan")
        L1.place(x=50,y=250)
        L2=Label(root3,text='2.SUV')
        L2.place(x=50,y=270)
        L3=Label(root3,text='3.Hatchback')
        L3.place(x=50,y=290)
        L4=Label(root3,text='4.Truck')
        L4.place(x=50,y=310)
        L5=Label(root3,text='5.Sports Car')
        L5.place(x=50,y=330)
        L6=Label(root3,text='6.Minivan')
        L6.place(x=50,y=350)
        L7=Label(root3,text='Enter your choice')
        L7.place(x=100,y=370)
        x2=tkinter.Entry(root3)
        x2.place(x=200,y=370)
        
        L7=Label(root3,text=('enter date')).place(x=100,y=400)
        x3=tkinter.Entry(root3)
        x3.place(x=200,y=400)

        L8=Label(root3,text=('enter time in 24 hour format')).place(x=48,y=430)
        x4=tkinter.Entry(root3)
        x4.place(x=200,y=430)
        
        B1=Button(root3,text='Submit',command=apo_details)
        B1.place(x=120,y=480)   
        root3.resizable(False,False)
        root3.mainloop()



# For AADHAAR no input
def apoint():
    global x1
    root2=Tk()
    label=Label(root2,text="BOOKING",font='arial 25 bold')
    label.pack()
    frame=Frame(root2,height=200,width=200)
    frame.pack()
    l1=Label(root2,text="AADHAAR NO.")
    l1.place(x=10,y=130)
    x1=tkinter.Entry(root2)
    x1.place(x=100,y=130)
    b1=Button(root2,text='Submit',command=get_apoint)
    b1.place(x=100,y=160)
    root2.resizable(False,False)
    root2.mainloop()
    
# List of doctors
def lst_doc():
    root4=Tk()
    
    l=["Nissan Versa","Toyota Corolla","Honda Civic","Suzuki Vitara","Jeep Cherokee"," Volkswagen Polo","Audi A3","Ford F150","Dodge Ram","Maserati Quattroporte",'Porsche 911','Dodge Grand Caravan',
       'Honda Odyssey','Toyota Sienna']
    m=["Sedan","Sedan","Sedan","SUV","SUV","Hatchback","Hatchback","Truck","Truck",
       "Sports Car",'Sports Car','Minivan','Minivan','Minivan']
    n=[250,250,300,250,350,270,350,300,370,480,550,400,300,340]

    frame=Frame(root4,height=500,width=500)
    frame.pack()
    
    
    l1=Label(root4,text='NAME OF CARS') 
    l1.place(x=20,y=10)
    count=20
    for i in l:
       count=count+20
       l=Label(root4,text=i)
       l.place(x=20,y=count)

    l2=Label(root4,text='TYPE')
    l2.place(x=140,y=10)
    count1=20
    for i in m:
       count1=count1+20
       l3=Label(root4,text=i)
       l3.place(x=140,y=count1)

    l4=Label(root4,text='RENT (IN $)')
    l4.place(x=260,y=10)
    count2=20
    for i in n:
       count2=count2+20
       l5=Label(root4,text=i)
       l5.place(x=260,y=count2)
    root.resizable(False,False)
    root4.mainloop()

def ser_avail():
    
    root5=Tk()
    frame=Frame(root5,height=500,width=500)
    frame.pack()
    l1=Label(root5,text='SERVICES AVAILABLE')
    l1.place(x=20,y=10)
    f=["Car Rental","Doorstep Delivery","Assistance","Insurance","Maintenance","Replacement","Chauffeur Services","Long Term Rent"]
    count1=20
    for i in f:
       count1=count1+20
       l3=Label(root5,text=i)
       l3.place(x=20,y=count1)
    l2=Label(root5,text='TABLE NO')
    l2.place(x=140,y=10)
    g=[1,2,3,4,5,6,7,8,]
    count2=20
    for i in g:
       count2=count2+20
       l4=Label(root5,text=i)
       l4.place(x=140,y=count2)
    l5=Label(root5,text='To avail any of these please contact on our no.:- 7306521876')
    l5.place(x=20,y=240)
    root5.resizable(False,False)
    root5.mainloop()

def modify():
    global x3,x4,choice,new,x5,root6
    p1=x3.get()
    cur.execute('select * from booking where idno=(%s)',(p1,))
    
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else: 
      root6=Tk()
      frame=Frame(root6,height=500,width=500)
      frame.pack()
      l1=Label(root6,text='DATA MODIFICATION',font="arial 15 bold")
      l1.place(x=75,y=10)
      l2=Label(root6,text='WHAT YOU WANT TO CHANGE')
      l2.place(x=50,y=200)
      l3=Label(root6,text='1.NAME')
      l3.place(x=50,y=220)
      l4=Label(root6,text='2.AGE')
      l4.place(x=50,y=240)
      l5=Label(root6,text='3.GENDER')
      l5.place(x=50,y=260)
      l6=Label(root6,text='4.PHONE')
      l6.place(x=50,y=280)
      l7=Label(root6,text='5.CITY')
      l7.place(x=50,y=300)
      x2=Label(root6,text='Enter')
      x2.place(x=50,y=330)
      x4=tkinter.Entry(root6)
      choice=x4.get()
      x4.place(x=100,y=330)
      for i in dat:
            name=Label(root6,text='NAME:-')
            name.place(x=50,y=80)
            name1=Label(root6,text=i[1])
            name1.place(x=150,y=80)
            age=Label(root6,text='AGE:-')
            age.place(x=50,y=100)
            age1=Label(root6,text=i[2])
            age1.place(x=150,y=100)
            gen=Label(root6,text='GENDER:-')
            gen.place(x=50,y=120)
            gen1=Label(root6,text=i[3])
            gen1.place(x=150,y=120)
            pho=Label(root6,text='PHONE:-')
            pho.place(x=50,y=140)
            pho1=Label(root6,text=i[4])
            pho1.place(x=150,y=140)
            bg=Label(root6,text='CITY:-')
            bg.place(x=50,y=160)
            bg1=Label(root6,text=i[5])
            bg1.place(x=150,y=160)
      b=Button(root6,text='Submit',command=do_modify)
      b.place(x=50,y=400)
      L1=Label(root6,text='OLD DETAILS')
      L1.place(x=50,y=50)
      L2=Label(root6,text='ENTER NEW DETAIL')
      L2.place(x=50,y=360)
      x5=tkinter.Entry(root6)
      new=x5.get()
      x5.place(x=160,y=360)

      root6.resizable(False,False)
      root6.mainloop()

def do_modify():
    global ad,x3,x4,x5
    ad=x3.get()
    choice=x4.get()
    new=x5.get()
    if choice=='1':
        cur.execute('update booking set name={} where idno={}'.format(new,ad))
    elif choice=='2':
        cur.execute('update booking set age={} where idno={}'.format(new,ad))        
    elif choice=='3':
        cur.execute('update booking set gender={} where idno={}'.format(new,ad))
    elif choice=='4':
        cur.execute('update booking set phone={} where idno={}'.format(new,ad))    
    elif choice=='5':
        cur.execute('update booking set bg={} where idno={}'.format(new,ad))
    else:
        pass
    root6.destroy()
    tkinter.messagebox.showinfo("DONE", "YOUR DATA HAS BEEN MODIFIED")
    
choice=None
new=None    
ad=None
def mod_sub():
    global x3,ad
    root7=Tk()
    label=Label(root7,text="MODIFICATION",font='arial 25 bold')
    label.pack()
    frame=Frame(root7,height=200,width=200)
    frame.pack()
    l1=Label(root7,text="AADHAAR NO.")
    l1.place(x=10,y=130)
    x3=tkinter.Entry(root7)
    x3.place(x=100,y=130)
    ad=x3.get()
    b1=Button(root7,text='Submit',command=modify)
    b1.place(x=100,y=160)
    root7.resizable(False,False)
    root7.mainloop()     

def search_data():
    global x3,ad
    root7=Tk()
    label=Label(root7,text="SEARCH DATA",font='arial 25 bold')
    label.pack()
    frame=Frame(root7,height=200,width=200)
    frame.pack()
    l1=Label(root7,text="AADHAAR NO.")
    l1.place(x=10,y=130)
    x3=tkinter.Entry(root7)
    x3.place(x=100,y=130)
    ad=x3.get()
    b1=Button(root7,text='Submit',command=view_data)
    b1.place(x=100,y=160)
    root7.resizable(False,False)
    root7.mainloop()

def view_data():
    global p1
    p1=x3.get()
    cur.execute('select * from booking where idno=(%s)',(p1,))
    
    dat=cur.fetchall()
    print(dat)
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        det=a
        tkinter.messagebox.showinfo("BOOKING DETAILS",det)
        
   
root=Tk()
label=Label(root,text="CAR RENTAL",font="arial 40 bold",bg='light blue')
b1=Button(text="Registration",font="arial 20 bold",bg='yellow',command=register)
b2=Button(text="Booking",font="arial 20 bold",bg='yellow',command=apoint)
b3=Button(text="List of Cars",font="arial 20 bold",bg='yellow',command=lst_doc)
b4=Button(text="Services available",font='arial 20 bold',bg='yellow',command=ser_avail)
b7=Button(text="View data",font='arial 20 bold',bg='yellow',command=search_data)
b5=Button(text="Modify existing data",font='arial 20 bold',bg='yellow',command=mod_sub)
b6=Button(text="Exit",font='arial 20 bold',command=root.destroy,bg='violet')
label.pack()
b1.pack(side=LEFT,padx=10)
b3.pack(side=LEFT,padx=10)
b4.pack(side=LEFT,padx=10)
b2.place(x=25,y=500)
b7.pack(side=LEFT,padx=10)
b5.place(x=350,y=500)
b6.place(x=750,y=500)
frame=Frame(root,height=600,width=50)
frame.pack()
root.resizable(False,False)
root.mainloop()