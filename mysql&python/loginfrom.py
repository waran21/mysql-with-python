from select import select
from mysql.connector import cursor,connect
import getpass as gs
from owener import hii
from emptab import emp,lot
def err():
    try:
        coun=0
        while True:
            con=connect(user='root',password='your pass word',host='dns',database='your database name')
            cn=con.cursor()
            j=input('enter user name: ')
            hj=gs.getpass(prompt="enter your pin")
            n="select * from owner where name='%s' and password='%s'"
            vn=cn.execute(n %(j,hj)) 
            ch=cn.fetchall()
            for i in ch:
                if (i[0]==j and i[1]==hj):
                    print("welcome")
                    print('-'*30)
                    hii()
                    break
            print("invaid pin")
            coun=coun+1
            if(coun==3):
                print("contact the office:")
                break       
    except ValueError:
        print("bdabase was not connect:...")
def empp():
    try:
        coun=0
        while True:
            con=connect(user='root',password='your pass word',host='dns',database='your database name')
            cn=con.cursor()
            j=input('enter user name: ')
            hj=input("enter the passwd")
            n="select * from newemp1 where name='%s' and pasword='%s'"
            vn=cn.execute(n %(j,hj)) 
            ch=cn.fetchall()
            for i in ch:
                if (i[1]==j and i[2]==hj):
                    print("welcome")
                    print("-"*35)
                    emp()
                    lot()
                    break #pasword # id, name, pasword, sal
            print("invaid pin")
            coun=coun+1
            if(coun==3):
                print("contact the office:")
                break       
    except ValueError:
        print("bdabase was not connect:...")
    