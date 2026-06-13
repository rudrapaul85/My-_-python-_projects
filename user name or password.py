username= "rudra"
password= "1234"
type = "guest"
while True:
    name = input("enter your name :")
    if name == username :
        print("user name matched " )
        lock = input("enter your password :")
        if lock == password:
            print("password matched :")
            break 
    elif name == type:
            print("no password needed ")
            break
    else :
        print (" user name is not matched " )