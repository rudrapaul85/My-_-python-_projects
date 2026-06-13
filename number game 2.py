#write a code where i guess random the swcrect number . it have 5 lives to get the number:
import random
secret = random.randint(1,60)
print("welcom to the guess number game")
while True:
    print("now we are start the game")
    for lives in range(1,6):
        print ("lives lift :",lives)
        guess = int(input ("guess 1 to 60:"))
        if secret == guess:
            print("you win the game")
            break
        elif secret > guess:
            print("your number is low")
        elif secret < guess:
            print("your number is high")
        if lives == 5 and guess != secret:
                print ("gameover ")
    restart = input("can u restart the game? (YES or NO) :")
    if restart.lower() =="no":
                    print ("thanks for playing ")
                    break
                   
       
       
       
        
    
    
       