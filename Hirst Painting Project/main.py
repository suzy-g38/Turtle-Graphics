import turtle as t
from turtle import Screen
import random

color_list = [(205, 155, 102), (54, 97, 138), (141, 160, 190), (146, 86, 57), (197, 143, 167), (22, 44, 58), (232, 208, 107), (144, 69, 93), (177, 156, 47), (63, 120, 85), (193, 87, 121), (205, 89, 66), (138, 175, 154), (224, 170, 189), (61, 43, 33), (103, 120, 168), (13, 57, 46), (180, 186, 213), (9, 98, 72), (44, 58, 101), (56, 34, 41), (87, 155, 106), (229, 174, 164), (99, 45, 62), (228, 207, 13), (108, 44, 38), (10, 89, 103), (54, 154, 171), (73, 72, 39), (170, 205, 190), (160, 204, 213)]

tim = t.Turtle()

t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1,number_of_dots+1):
    tim.dot(5, random.choice(color_list))
    tim.forward(10)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(10)
        tim.setheading(180)
        tim.forward(100)
        tim.setheading(0)

    ##tim.dot(random.choice(color_list))
    #tim.pendown()
    #tim.left(90)
    #vertical_move()
    #tim.right(90)
    #tim.penup()
    #tim.forward(10)
    ##tim.dot(random.choice(color_list))
    #tim.pendown()
    #tim.right(90)





    #vertical_move()
        #tim.right(90)
        #tim.penup()
        #tim.forward(10)
        #tim.dot(random.choice(color_list))
        #tim.pendown()
        #tim.right(90)





screen= Screen()
screen.exitonclick()
