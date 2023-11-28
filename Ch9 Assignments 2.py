

# Upper and lower limits are both exclusive
def guessing_game(lower_bound: int, upper_bound: int, full_range_start, full_range_end, game_type:int):
    game_state = True
    error_count = 0 
    
    while game_state:
        #Modification to make: The below input could use a variable for the first half if I 
        # don't want the message to appear everytime they put in a number 
        try:
            if game_type == 1:
                guess = int(input("Guess a number outside the range "+str(full_range_start)+"-"+str(full_range_end)+": "))
            else:
                guess = int(input("Guess a number between "+str(full_range_start)+" - "+str(full_range_end)+": "))
            
        except:
            print("Invalid input")
            error_count +=1
            if error_count > 2:
               print("What are you stupid?... Red eye flashes twice\n")
               game_state = False
               
        if guess > lower_bound and guess < upper_bound and game_type == 0:
            game_state = False
            print("Congrats! You win!")
            print("Your guess was:",guess)
        elif guess < lower_bound or guess > upper_bound and game_type == 1:
            game_state = False
            print("Congrats! You win!")
            print("Your guess was:",guess)
        else:
            print("Guess again!")
       
    if input("Do you want to play again? (y/n): ").lower() == "y":
        guessing_game(lower_bound, upper_bound, full_range_start, full_range_end, game_type)



#guessing_game(89, 100, 1, 100, 0)
#guessing_game(-60, -49, -100, 0, 0)
#guessing_game(0, 5, 0, 5, 1)
#guessing_game(12344, 12346, -1_000_000, 1_000_000, 0)






