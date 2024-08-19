import random

randomNumber = random.randint(1, 100)
print(randomNumber)
userGuess = int(input("Guess a number between 1 and 100: "))
guessCount = 1

while (userGuess != randomNumber):
    if userGuess > randomNumber:
        print("Number too high!")
        guessCount += 1
        userGuess;
    elif userGuess < randomNumber: 
        print("Number too low!")
        guessCount += 1
   
    userGuess = int(input("Not a match, Guess again: "))
    
if guessCount == 1: 
    print(f"{guessCount} attempt, you won on your first try!")
else:
    print(f"{guessCount} Attempts: You win")