import turtle as t
from turtle import Screen
import random


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles=[0,90,180,270]
tim = t.Turtle()
tim.pensize(15)
tim.shape("circle")
#tim.speed("fastest")
t.colormode(255)

for i in range(random.randint(1,300)):
    #tim.color(random.choice(colors))
    tim.pencolor((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
    tim.forward(30)
    tim.setheading(random.choice(angles))
    tim.speed(i)


screen= Screen()
screen.exitonclick()