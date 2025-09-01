from turtle import Turtle, Screen

# Create a turtle object
timmy = Turtle()

# Print the type of the turtle object
print(type(timmy))

# Make the turtle do something visible
timmy.shape("turtle")
timmy.color("red", "green")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)

# Create a screen object to keep the window open
screen = Screen()
screen.exitonclick()  # Click to close the window
