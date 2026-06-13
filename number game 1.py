import random

secret_number = random.randint(1, 60)
print("Welcome to the game!")

while True:
    print("Starting a new game...")
    
    for lives in range(1, 6):
        print("Lives left:", lives)
        guess = int(input("Guess 1 to 60: "))
        
        if guess == secret_number:
            print("You win!")
            break
        elif guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
            
        if lives == 5:
            print("Game Over!")
            
    restart = input("Play again? (yes/no): ")
    if restart.lower() == "no":
        print("Thanks for playing!")
        break
        