#rebborg challenge = https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

print('''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

#draw square
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
# it will loop until it is true 
while at_goal() != True;
    jump()
      

      or 


while not atgoal():
      jump()
      ''')


# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# hurdle 3
print('''
      
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

#draw square
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
# it will loop until it is true 
while at_goal() != True:
      if wall_infront():
         jump()
      else:
        move()
      
      
      ''')


#hurdle 4
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# list of walls 

