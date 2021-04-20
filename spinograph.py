import turtle as t
from turtle import Screen
import random

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r,g,b)
    return color

tim = t.Turtle()
#tim.color(random_color())
t.colormode(255)


tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.circle(100)
        tim.pencolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        tim.setheading(tim.heading() + size_of_gap)




draw_spirograph(5)












screen= Screen()
screen.exitonclick()