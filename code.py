import tabulate
import mysql.connector
import datetime
con=mysql.connector.connect(host='localhost',user='root',password='sql123',database='project')
cur=con.cursor()
#cur.execute("create database SCHOOL")
def adminloop():
    while True:
        ch=int(input("admin module\n1. movie \n2. client\n3. addon"))
        if ch==1:
            x=int(input("1 for display\n2 for add\n3 for delete\4 from modify"))
            if x==1:
                displaymovadmin()
            if x==2:
                addmovie()
            if x==3:
                deletemovie()
            if x==4:
                modify()
        elif ch==2:
            x=int(input("1 for display\n2 for add\n3 for delete\4 from modify"))
            if x==1:
                clientdisplay()
            if x==2:
                clientadd()
            if x==3:
                deleteclient()
        elif ch==3:
            x=int(input("1 for display\n2 for add\n3 for delete\4 from modify"))
            if x==1:
                displayaddon()
            if x==2:
                addaddon()
            if x==3:
                deleteaddon()
            if x==4:
                modifyaddon()
        
            

def mainlogin():
    import tkinter
    from tkinter import messagebox
    window = tkinter.Tk()
    window.title("Login Page using Python for admin")
    window.geometry('750x550')
    window.configure(bg='#8F00FF')
    def login():
        username = "hkrgk"
        password = "admin"

        if username_entry.get()==username and password_entry.get()==password:
            messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
            while True:
                ch=int(input("admin module\n1. movie \n2. client\n3. addon"))
                if ch==1:
                    x=int(input("1 for display\n2 for add\n3 for delete\n4 from modify"))
                    if x==1:
                        displaymovadmin()
                    if x==2:
                        addmovie()
                    if x==3:
                        deletemovie()
                    if x==4:
                        modify()
                    
                elif ch==2:
                    x=int(input("1 for display\n2 for add\n3 for delete\n4 for modify"))
                    if x==1:
                        clientdisplay()
                    if x==2:
                        clientadd()
                    if x==3:
                        deleteclient()
                elif ch==3:
                    x=int(input("1 for display\n2 for add\n3 for delete\n4 from modify"))
                    if x==1:
                        displayaddon()
                    if x==2:
                        addaddon()
                    if x==3:
                        deleteaddon()
                    if x==4:
                        modifyaddon()
                ch=input("y or n")
                if ch in 'Nn':
                    break
                
        
            
            
        else:
            messagebox.showerror(title="Error", message="Invalid login.")
            
            

    frame = tkinter.Frame(bg='#8F00FF')
    login_label = tkinter.Label(frame, text="MovieMate-admin login", bg='#000000', fg="#DC143C", font=("Arial", 30))
    username_label = tkinter.Label(frame, text="Username", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'))
    password_label = tkinter.Label(frame, text="Password", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'))
    username_entry = tkinter.Entry(frame, font=("Arial", 16))
    password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    login_button = tkinter.Button(frame, text="Login", bg="#DC143C", fg="#FFFFFF", font=("Arial", 16), command=login)
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)
    frame.pack()
    window.mainloop()



def mainlogin1():
   
    import tkinter
    from tkinter import messagebox
    window = tkinter.Tk()
    window.title("Login Page using Python")
    window.geometry('750x550')
    window.configure(bg='#8F00FF')
    def login():
        username = "userpj"
        password = "9999"
       

        if username_entry.get()==username and password_entry.get()==password:
            messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
            while True:
                ch=int(input("1 for display movies\n2 for selecting movie\n3 for viewing addon table\n4 for selecting addon\n5 for viewing bill"))
                if ch==1:
                    displaymov()
                if ch==2:
                    select()
                if ch==3:
                    displayadd()
                if ch==4:
                    selectmenu()
                if ch==5:
                    bill()
                    break

            
        else:
            messagebox.showerror(title="Error", message="Invalid login.")
            
            

    frame = tkinter.Frame(bg='#8F00FF')
    login_label = tkinter.Label(frame, text="MovieMate", bg='#000000', fg="#DC143C", font=("Arial", 30))
    username_label = tkinter.Label(frame, text="Username", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'))
    password_label = tkinter.Label(frame, text="Mobile Number", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'))
    username_entry = tkinter.Entry(frame, font=("Arial", 16))
    password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
    login_button = tkinter.Button(frame, text="Login", bg="#DC143C", fg="#FFFFFF", font=("Arial", 16), command=login)
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)
    frame.pack()
    window.mainloop()


'''def cover():
    print("Welcome to Movie Mate")
    print("Enter the following numbers for the respective commands:")
    ch=int(input("1.for admin 2.for user"))
    if ch==1:
        mainlogin()
    elif ch==2:
        mainlogin1()
        
cover()'''
    

    
def createfun():
    cur.execute('create table movie3(Serial_No int,Movie_Name varchar(20),Rating float(4,2),Language varchar(20),Cost int)')

#admin
def add():
    cur.execute("insert into movie3 values(1,'Avatar',9.2,'English',450)")
    cur.execute("insert into movie3 values(2,'3 Idiots',9.0,'Hindi',300)")
    cur.execute("insert into movie3 values(3,'KGF',6.5,'Kannada',350)")
    cur.execute("insert into movie3 values(4,'Avengers',8.5,'English',550)")
    cur.execute("insert into movie3 values(5,'Grown ups',7.2,'English',250)")



def displaymovadmin():
    cur.execute("select * from movie3")
    data=cur.fetchall()
    heading=['Serial_No','Movie Name','Rating','Language','Cost per ticket']
    print(tabulate.tabulate(data,headers=heading))

def addmovie():
    while True:
        s=int(input("serial number"))
        mn=input("movie name")
        r=float(input("rating"))
        l=input("language")
        c=int(input("cost"))
        query="insert into movie3 values({},'{}',{},'{}',{})".format(s,mn,r,l,c)
        cur.execute(query)
        con.commit()
        print("movie added")
        ch=input("y or n")
        if ch in 'n':
            break
        else:
            continue
            
        
        

def deletemovie():
    x=int(input("serial number of movie to be deleted"))
    cur.execute("delete from movie3 where Serial_no={}".format(x))
    print("movie deleted")

def modify():
    y=int(input("serial number of movie whose cost to be changed"))
    x=int(input('new cost'))
    cur.execute("update movie3 set cost={} where Serial_no={}".format(x,y))
    print("value updated")

#client
def client():
    cur.execute('create table client(Serial_No int,name varchar(80),card_number int)')


def clientadd():
    sn=int(input("enter serial number"))
    n=input("enter name")
    cn=int(input("enter card number"))
    cur.execute("insert into client values({},'{}',{})").format(sn,n,cn)
    cur.execute(query)
    con.commit()


def clientdisplay():
    cur.execute("select * from client")
    data=cur.fetchall()
    heading=['Serial_No','Name','card number']
    print(tabulate.tabulate(data,headers=heading))

def deleteclient():
    x=int(input("serial number of movie to be deleted"))
    cur.execute("delete from client where Serial_no={}".format(x))
    print("client deleted")

def displayaddon():
    cur.execute("select * from addon1")
    data=cur.fetchall()
    heading=['Serial_No','item Name','cost']
    print(tabulate.tabulate(data,headers=heading))

def deleteaddon():
    x=int(input("serial number of addon to be deleted"))
    cur.execute("delete from addon where Serial_no={}".format(x))
    print("addon deleted")

def addaddon():
    while True:
        s=int(input("serial number"))
        mn=input("item name")
        c=int(input("cost"))
        query="insert into addon1 values({},'{}',{})".format(s,mn,c)
        cur.execute(query)
        con.commit()
        print("addon added")
        ch=input("y or n")
        if ch in 'n':
            break
        else:
            continue

def modifyaddon():
    y=int(input("serial number of addon whose cost to be changed"))
    x=int(input('new cost'))
    cur.execute("update addon1 set Cost={} where Serial_no={}".format(x,y))
    print("value updated")





    
    
    


def addons():

    cur.execute('create table addon1(Serial_No int primary key,Item varchar(80),Cost int)')



def menu():
    cur.execute("insert into addon1 values(1,'Club',450)")
    cur.execute("insert into addon1 values(2,'cappucino',300)")
    cur.execute("insert into addon1 values(3,'brownie',350)")
    cur.execute("insert into addon1 values(4,'popcorn',550)")
    cur.execute("insert into addon1 values(5,'soft',250)")


def displaymov():
    cur.execute("select * from movie3")
    data=cur.fetchall()
    heading=['Serial_No','Movie Name','Rating','Language','Cost per ticket']
    print(tabulate.tabulate(data,headers=heading))



def select():
    
    global x
    x=int(input("Enter serial no of movie you wish to watch"))
    cur.execute("Select * from movie3 where Serial_No={}".format(x))
    data=cur.fetchall()
    heading=['serial no','Movie Name','Rating','Language','Cost per ticket']
    print(tabulate.tabulate(data,headers=heading))
    cur.execute("Select Movie_Name,Cost from movie3 where Serial_No={}".format(x))
    global jay
    jay=cur.fetchall()
    global n
    n=int(input("no of tickets"))
    cur.execute("select Cost from movie3 where Serial_No={}".format(x))
    data=cur.fetchall()
    
    global jay2
    for i in data:
        for j in i:
            print(j)
    global total
    total=n*j
    print(total)

def displayadd():
    cur.execute("select * from addon1")
    data=cur.fetchall()
    heading=['Serial_No','Item Name','Cost']
    print(tabulate.tabulate(data,headers=heading))



def selectmenu():
    global x1
    global total1
    x1=int(input("Enter sno of Item you wish to purchase"))
    cur.execute("Select * from addon1 where Serial_No={}".format(x1))
    data=cur.fetchall()
    heading=['serial no','Item Name','Cost']
    print(tabulate.tabulate(data,headers=heading))
    cur.execute("Select Item,Cost from addon1 where Serial_No={}".format(x1))
    global jay1
    jay1=cur.fetchall()
    global n1
    n1=int(input("quantity"))
    cur.execute("select Cost from addon where Serial_No={}".format(x1))
    for i in data:
        for j in i:
            print(j)
   
    total1=n1*j
    
    
    


def discount():
    q=datetime.datetime.now()
    y=q.strftime("%A")
    l1=['Friday','Saturday','Sunday']
    l2=['Monday','Wednesday']
    global d
    d=0
    if y in l1:
        d=0.3
    elif y in l2:
        d=0.1

def totalbill():
    discount()
    global fx
    global fa
    global total,total1
    
    fx=total+total1
    fa=fx-(d*fx)

def billtable():
    global fx
    global fa
    global x,n,x1,n1,d
    totalbill()
    global jay2
    jay2=[fx,d,fa]
    print(x,n,x1,n1,d,fx,fa)
    

def bill():
    billtable()
    global jay,jay1,jay2
    print(jay,jay1,jay2)
    k=[]
    for i in jay:
        for j in i:
            k+=[str(j)]
    for d in jay1:
        for l in d:
            k+=[str(l)]
    for m in jay2:
        k+=[str(m)]
    d=()
    for i in k:
        d+=(i,)
    a=[]
    a+=(d,)
    print(a)

    heading=['movie name','movie price','addon name','addon price','total price','discount','final price']
    print(tabulate.tabulate(a,headers=heading))
    
    


        
            
    
            


#mainlogin()
def cover():
    print("Welcome to Movie Mate")
    print("Enter the following numbers for the respective commands:")
    ch=int(input("1.for admin 2.for user"))
    if ch==1:
        mainlogin()
    elif ch==2:
        mainlogin1()
        
cover()
                 

'''while True:
    
    ch=int(input("1 or 2 or 3 or 4 or 5 or 6 or 7"))
    if ch==1:
        ()
    if ch==3:
        displaymov()
    if ch==4:
        select()
    if ch==2:
        add()
    if ch==5:
        addons()
    if ch==6:
        menu()
    if ch==7:
        displayadd()
    if ch==8:
        selectmenu()'''