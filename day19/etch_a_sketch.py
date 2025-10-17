# sketch drawing using turtle directions 
#  https://docs.python.org/3/library/turtle.html#turtle-motion

from turtle import Turtle, Screen

diwa = Turtle()

screen = Screen()


def move_forward():
    diwa.forward(10)
def move_backwards():
    diwa.backward(10)
def turn_left():
    new_heading = diwa.heading() + 10
    diwa.setheading(new_heading)
def turn_right():
    new_heading = diwa.heading() - 10
    diwa.setheading(new_heading)
def clear():
    diwa.clear()
    # it will draw while cleaning up 
    diwa.penup()
    diwa.home()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()