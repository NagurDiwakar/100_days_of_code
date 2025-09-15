from turtle import Turtle, Screen
import random



t = Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
turtle.colormode(255)


directions = [0,90,180,270]
t.pensize(10)
t.speed(0) 
## or t.speed("fastest")



for _ in range(200):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))







