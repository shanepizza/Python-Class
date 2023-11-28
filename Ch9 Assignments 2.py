

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


def star_row(num_stars:int, justify:str, given_rows:int):
    a = ""
    b = ""
  #assign a fixed value (i.e. 20) to set the frame width. The default width is the number of rows. 
  #ex: 10 rows, 10 collumns  
    used_rows = 20
    #used_rows = given_rows
    
#justify to the left
    if justify == "center":
      #This will figure out how manuy spaces are needed on the left based on how many
      # stars need to fit in the row
        num_spaces = (used_rows*2 - num_stars)//2
      #Assigns all the needed spaces and stars to the variables a and b  
        for i in range(num_spaces):
            a = a+" "
        a = a[num_stars//2:]
        for i in range(num_stars):
          #special case since the diamond needs to grow by two stars each time
            if i < 1:
                b = "*"
            else:
                b = b+"**"

 #justify to the right       
    elif justify == "right":
      #Spaces start out the entire length of the row but will shrink one for every star needed  
        num_spaces = used_rows -num_stars
      #Assigns all the needed spaces and stars to the variables a and b  
        for i in range(num_spaces):
            a = a + " "
        for i in range(num_stars):
            b = b +"*"

  #left justification will be the default.
    else:
      #size of the printing area is determined by the number of rows
        num_spaces = used_rows
      #Assigns all the needed spaces and stars to the variables a and b 
        for i in range(num_stars):
            a = a+"*"
        for i in range(num_spaces):
            b = b+" "
#print the row   
    print(a, end="")
    print(b)
        
already_ran = False
def draw_star_pattern(rows:int, justify:str, state:int):
    global already_ran      
    for i in range(rows):
        a = i+1
        
      #state determines if the rows are printed in ascending or descending order
      #-1 is descending; any other integer will default to ascending  
        if state == -1:
            a = rows+(-1*i)
        star_row(a, justify, rows)
    if justify == "center" and already_ran == False:
        already_ran = True
        draw_star_pattern(rows-1, justify, state*-1)

def draw_shapes():
    keep_drawing = True
    while keep_drawing == True:
        try:
            shape_size = int(input("please enter the size of the next shape. (x to exit): "))
            
            shape_type = input("How should the shape justify? (left, right, center): ")
        except Exception as error:
            print("How did he do it?", error)
            draw_star_pattern(10, "left", 0)
        if shape_type.lower() == "center":
            draw_star_pattern(shape_size//2, "center", 0)
        elif shape_type.lower() == "right":
            draw_star_pattern(shape_size, "right", -1)
        else:
            draw_star_pattern(shape_size, "left", 0)

        cont = input("Create another shape? (y/n): ")
        if cont.lower() == "n":
            keep_drawing == False
        




#guessing_game(89, 100, 1, 100, 0)
#guessing_game(-60, -49, -100, 0, 0)
#guessing_game(0, 5, 0, 5, 1)
#guessing_game(12344, 12346, -1_000_000, 1_000_000, 0)

draw_shapes()





