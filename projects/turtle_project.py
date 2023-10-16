"""Project for exploring the uses of Turtles"""
from turtle import *
from math import *

bob: Turtle = Turtle()
screen: Screen = Screen()

screen.setup(1200,650)

bob.speed(0)
bob.degrees()


def line(turt: Turtle, start_pos: list[int], end_pos: list[int]):
    """Creates a line between any two points"""
    turt.teleport(start_pos[0],start_pos[1])
    distance: float = sqrt((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)
    angle: float = atan((end_pos[1]-start_pos[1])/(end_pos[0]-start_pos[0]))
    turt.setheading(angle)
    turt.pendown()
    turt.forward(distance)

def draw_rect(turt: Turtle, top_left: list[int], bottom_right: list[int]):
    turt.penup()
    turt.goto(top_left[0],top_left[1])
    turt.pendown()
    turt.begin_fill()
    turt.setheading(0)
    rect_width: int = abs(top_left[0]-bottom_right[0])
    rect_height: int = abs(top_left[1]-bottom_right[1])
    i: int = 0
    while i < 2:
        turt.forward(rect_width)
        turt.right(90)
        turt.forward(rect_height)
        turt.right(90)
        i += 1
    turt.end_fill()

def draw_triangle(turt: Turtle, size: float):
    turt.setheading(0)
    turt.forward(20*size)
    turt.left(120)
    i: int = 0
    while i < 2:
        turt.forward(40*size)
        turt.left(120)
        i += 1
    turt.forward(20*size)

def draw_tree(turt: Turtle, size: float, trunk_position: list[int], hex_code: str):
    turt.color(hex_code, hex_code)
    turt.setposition(trunk_position[0],trunk_position[1])
    i: int = 1
    while i <=7:
        turt.pendown()
        turt.begin_fill()
        draw_triangle(turt,size)
        turt.penup()
        turt.end_fill()
        turt.setposition(trunk_position[0],(trunk_position[1]+(size*10*i)))
        turt.pendown()
        turt.begin_fill()
        draw_triangle(turt,0.75*size)
        turt.penup()
        turt.end_fill()
        turt.setposition(trunk_position[0],(trunk_position[1]+(size*10*i)))
        i += 1


def main():
    bob.color("#c37f84", "#c37f84")
    draw_rect(bob, [-600,325], [600,175])
    bob.color("#e1a063","#e1a063")
    draw_rect(bob,[-600,175],[600,50])
    bob.color("#e9ba7b","#e9ba7b")
    draw_rect(bob,[-600,50],[600,-200])
    bob.color("grey","dark grey")
    bob.goto(75,-50)
    bob.pendown()
    bob.begin_fill()
    bob.goto(-240,240)
    bob.goto(-600,50)
    bob.goto(-600,-50)
    bob.goto(75,-50)
    bob.end_fill()
    bob.penup()
    bob.goto(60,70)
    bob.pendown()
    bob.begin_fill()
    bob.goto(60,70)
    bob.goto(-60,-50)
    bob.goto(600,-50)
    bob.goto(60,70)
    bob.end_fill()
    bob.penup()
    bob.goto(-300,-50)
    bob.pendown()
    bob.begin_fill()
    bob.goto(-100,80)
    bob.goto(100,-50)
    bob.goto(-300,-50)
    bob.end_fill()
    bob.penup()
    bob.color("#809298","#809298")
    bob.goto(-600,-50)
    bob.pendown()
    bob.begin_fill()
    bob.goto(600,-35)
    bob.penup()
    bob.goto(600,-325)
    bob.goto(-600,-325)
    bob.goto(-600,-50)
    bob.end_fill()
    bob.penup()
    bob.color("#4f6a53","#4f6a53")
    bob.goto(600,-20)
    bob.pendown()
    bob.begin_fill()
    bob.goto(-600,-280)
    bob.goto(600,-280)
    bob.goto(6000,-20)
    bob.penup()
    bob.end_fill()
    bob.goto(-600,-120)
    bob.color("#354529","#354529")
    bob.goto(600,-200)
    bob.goto(-600,-200)
    bob.goto(-600,-120)
    bob.penup()
    bob.end_fill()
    bob.color("#626638","#626638")
    bob.goto(600,-60)
    bob.pendown()
    bob.begin_fill()
    bob.goto(-600,-280)
    bob.goto(600,-280)
    bob.goto(600,-60)
    bob.end_fill()
    bob.penup()
    bob.color("#4f5d40","#4f5d40")
    bob.goto(-600,-140)
    bob.pendown()
    bob.begin_fill()
    bob.goto(-600,-325)
    bob.goto(350,-325)
    bob.goto(-600,-140)
    bob.penup()
    bob.end_fill()
    bob.color("#6d6a3f","#6d6a3f")
    bob.goto(-600,-275)
    bob.begin_fill()
    bob.pendown()
    bob.goto(600,-200)
    bob.goto(600,-325)
    bob.goto(-600,-325)
    bob.goto(-600,-275)
    bob.end_fill()
    bob.penup()
    draw_tree(bob,2.3,[-500,-210],"#292b1b")
    draw_tree(bob,1.8,[-510,-215],"#296211")
    draw_tree(bob,3,[-550,-250],"dark green")
    draw_tree(bob,1,[550,-55],"#296211")
    draw_tree(bob,0.9,[490,-75],"#292b1b")
main()
    
done()

