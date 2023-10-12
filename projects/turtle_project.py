"""Project for exploring the uses of Turtles"""
from turtle import *
from math import *

bob: Turtle = Turtle()
bob.radians()
bob.home()
bob.pencolor("blue")


def line(turt: Turtle, start_pos: list[int], end_pos: list[int]):
    """Creates a line between any two points"""
    turt.penup()
    turt.setheading(0)
    turt.setx(start_pos[0])
    turt.sety(start_pos[1])
    distance: float = sqrt((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)
    angle: float = atan((end_pos[1]-start_pos[1])/(end_pos[0]-start_pos[0]))
    print(distance)
    print(angle)
    turt.setheading(angle)
    turt.pendown()
    turt.forward(distance)


line(bob,[0,100],[200,300])


done()