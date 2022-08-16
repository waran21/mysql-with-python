from owndp import op,delemp,tottal
def hii():
    print("-"*45)
    print("\t1.add new emply \n\t2.delete the empty \n\t3.total sales")
    print("-"*35)
    ch=int(input('enter your choice: '))
    print("*"*35)
    if(ch==1):
        op()
    elif(ch==2):
        delemp()
    elif(ch==3):
        tottal()
    else:
        print("corect values: ")