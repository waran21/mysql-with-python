from mysql.connector import connect,cursor
import mysql.connector
#from recall import call
def usety():
    try:
        while True:
            dp=connect(user='root',password='your pass word',host='dns',database='your database name')
            print("welcome new user")
            print("compelt sery you enter the sum inputs for new user hear:")
            print("1.crete first user name aand pass word")
            print("2.create emply tabel")
            print("3.prodct tables:")
            print("4.temp tables: ")
            con=dp.cursor()
            n=int(input("enter your choice: "))
            if(n==1):
               qu="create table owner(name varchar(30),password varchar(8));"
               cv=con.execute(qu)
               mm=int(input("compelsery enter if u r open first time this one: "))
               if(mm==1):
                 nc=input("enter your name: ")
                 cv=input("enter your password: ")
                 qur="insert into owner value('%s','%s');"
                 con.execute(qur %(nc,cv))
                 dp.commit()
            elif(n==2):
                con.execute("create table newemp1(id varchar(8),name varchar(20),pasword varchar(12),sal float(8,2));")
            elif (n==3):
                print("create the prodcut tables: ")
                con.execute("create table prodct(id int(5),name varchar(13),cost int(5));")    
            elif (n==4):
                con.execute("create table temp12(id int(5),name varchar(13),cost int(5));")  
            dp.commit()
            print("table was creted")
    except ValueError:
       print("user data base was some problems")