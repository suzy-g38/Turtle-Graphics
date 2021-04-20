from turtle import Turtle, Screen
import random


timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for i in range(3,10):
    timmy.color(random.choice(colors))
    for j in range(i):
        timmy.forward(100)
        timmy.right(360/i)





screen= Screen()
screen.exitonclick()










