from turtle import Turtle, Screen
import random

t = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

for shape_side_n in range(3, 10):
    t.color(random.choice(colours))
    draw_shape(shape_side_n)



my_screen = Screen()
my_screen.exitonclick()




