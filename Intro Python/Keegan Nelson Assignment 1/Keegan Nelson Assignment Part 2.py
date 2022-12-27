from random import randint
    
print("Welcome to the guesing name")
answer = "yes"

while answer == "yes":
    secret = randint(1, 10)
    guess = 0
    while guess != secret: 
        g = input("Guess the number: ")
        guess = int(g)
        if  guess == secret:
            print("You win!")
        else:
            if guess > secret:
                print("Too High")
            else:
                print("Too Low")
    print("Game over!")
    answer = input("Do you want to play again, yes or no?") 

print("Game over! Have a great day!")







    
