import random
#ask to guess a number between 1 to 20:
guess_game = random.randint(1,20)
guess = int(input("guess the number between 1 to 20: "))
while guess != guess_game:  
      
#guess too high:
      if guess_game > guess:
         print("Too high! if the guess is greater than the random number")
        
#guess to low:
      elif guess_game < guess:
        print("Too low! if the guess is less than the random number") 
      guess = int(input("try again, guess the number between 1 to 20: "))
#guess right:
print("Correct! You sugessed it!")
exit()

      


              