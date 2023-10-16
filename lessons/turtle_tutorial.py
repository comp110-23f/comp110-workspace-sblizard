from turtle import Turtle, colormode, done
colormode(255)


leo: Turtle = Turtle()
leo.color(255,100,200)

leo.begin_fill()

i = 0
while i < 4:
    leo.left()
    leo.forward(100)
    i+=1

leo.end_fill()


done()