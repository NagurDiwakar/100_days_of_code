#https://docs.python.org/3/library/functions.html
# https://reeborg.ca/docs/en/#
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# huddle loop challenge
#https://www.udemy.com/course/100-days-of-code/learn/lecture/19115132#overview
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# drwaing the sqaure using two functions , raaborg 

print('''def turn_right():
    turn_left()
    turn_left()
    turn_left()


#draw square
def square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
   
square() ''')



# jump challenge

#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

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
    
    
    
for i in range(6):
    jump()

''')
