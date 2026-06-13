chocolate=10
maa=0

while True:
    give=int(input("how many chocolate givet to ur mom ?" ))
    if give <= chocolate:
        chocolate = chocolate - give
        maa = maa + give
        print("you give 1 chocolate to maa")
        print("left chocolate :",chocolate)
    else:
        print ("u r out of chocolate ")
        break
   # if chocolate == 0:
       #     print ("u r out of chocolate ")
         #   break
    
    

