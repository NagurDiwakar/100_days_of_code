from turtle import Turtle, Screen

my_turtle = Turtle()

my_turtle.shape("turtle")
my_turtle.color("green")
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)

## another method using  loop range

for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)


my_screen = Screen()
my_screen.exitonclick()



