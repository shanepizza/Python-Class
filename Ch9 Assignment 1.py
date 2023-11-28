

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
        

def draw_star_pattern(rows:int, justify:str, state:int):
    if state == -2:
          state = -1
          
    for i in range(rows):
        a = i+1
        
      #state determines if the rows are printed in ascending or descending order
      #-1 is descending; any other integer will default to ascending  
        if state == -1:
            a = rows+(-1*i)
        star_row(a, justify, rows)
        


draw_star_pattern(20, "right", 0)
print()
draw_star_pattern(20, "right", -1)
print()
draw_star_pattern(20, "left", 0)
print()
draw_star_pattern(20, "left", -1)
print()
draw_star_pattern(10, "center", 0)
draw_star_pattern(9, "center", -2)




   
