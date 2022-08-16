from mysql.connector import connect,cursor
def op():
    dp=connect(user='root',password='your pass word',host='dns',database='your database name')
    c=dp.cursor()
    print("add new emply...")
    nm=input("enter the emp unique id: ")
    nam=input("enter emp name: ")
    wor=input("enter the pass  word: ")
    sal=float(input("enter emp sal..."))
    ser="insert into newemp1 values('%s','%s','%s',%f);"
    c.execute(ser %(nm,nam,wor,sal))
    dp.commit()
    print("insert scussufully")
    print("-"*35)
def delemp():
    print("delet emp...")
    print("-"*35)
    dp=connect(user='root',password='your pass word',host='dns',database='your database name')
    c=dp.cursor()
    n=int(input('enter emp id...'))
    op="delete from newemp1 where id=%d;"
    c.execute(op %n)
    dp.commit()
    print("emp.. id was delted..")
    print("-"*35)
def tottal():
    con=connect(user='root',password='your pass word',host='dns',database='your database name')
    hj=con.cursor()
    c=0
    hj.execute("select * from prodct;")
    vv=hj.fetchall()
    print("*"*40)
    print("\tcode \titems \tcost")
    print("*"*40)
    if (vv !=None):
        for i in vv:
            c=c+i[2]
            for j in i:
                print("\t{}".format(j),end=' ')
            print()
    print("*"*40)
    print("\t \t total {}".format(c))
    print("*"*40)