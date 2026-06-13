password = input("creat a password :")
choose=(input("can u unlock this system ? :"))
if choose.lower()=="yes":
    enter_password=(input("enter the password :"))
    if enter_password==password :
        print("welcome user")
    else:
        print("wrong password ")
elif choose.lower()=="no":
    print("ok")

