from index import menu
from loginfrom import err,empp
import new_user as opi
import getpass as gs
from owener import hii
import sys
def call():
    while True:
        try:
            menu()
            ch= int(input('enter your choice'))
            print("-"*30)
            if (ch==1):
                print ("your selected the owner")
                err()
                break
            elif (ch==2):
                print("welcome employe")
                empp()
                break
            elif (ch==3):
                t=gs.getpass(prompt="enter the pin")
                i=0
                while True:
                    if(t=='1234'):
                        print("welcome new user:  ")
                        opi.usety()
                        break
                    i=i+1
                    print("invald pin")
                    if (i==3):
                        print("contact the company")
                        sys.exit()
                break
        except ValueError:
            print("invalid entry")
call()