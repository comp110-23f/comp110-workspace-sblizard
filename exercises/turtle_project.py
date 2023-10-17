"""Recreates Bob Ross's beautiful painting from the season 38 eposide "Grey Mountain"."""

__author__ = "730642587"
import random
from turtle import Turtle, done, Screen


def main() -> None:
    """Main function that will draw our beautiful scenery for us - returns None."""
    bob: Turtle = Turtle()
    screen = Screen()
    screen.setup(1200, 650)
    bob.speed(0)
    bob.degrees()
    bob.color("#c37f84", "#c37f84")
    draw_rect(bob, [-600, 325], [600, 175])
    bob.color("#e1a063", "#e1a063")
    draw_rect(bob, [-600, 175], [600, 50])
    bob.color("#e9ba7b", "#e9ba7b")
    draw_rect(bob, [-600, 50], [600, -200])
    draw_mount(bob, [75, -50], [-240, 240], [-600, -50])
    draw_mount(bob, [60, 70], [-60, -50], [600, -50])
    draw_mount(bob, [-300, -50], [-100, 80], [100, -50])
    bob.color("#809298", "#809298")
    bob.goto(-600, -50)
    bob.pendown()
    bob.begin_fill()
    bob.goto(600, -35)
    bob.penup()
    bob.goto(600, -325)
    bob.goto(-600, -325)
    bob.goto(-600, -50)
    bob.end_fill()
    bob.penup()
    bob.color("#4f6a53", "#4f6a53")
    bob.goto(600, -20)
    bob.pendown()
    bob.begin_fill()
    bob.goto(-600, -280)
    bob.goto(600, -280)
    bob.goto(6000, -20)
    bob.penup()
    bob.end_fill()
    bob.goto(-600, -120)
    bob.color("#354529", "#354529")
    bob.goto(600, -200)
    bob.goto(-600, -200)
    bob.goto(-600, -120)
    bob.penup()
    bob.end_fill()
    bob.color("#626638", "#626638")
    bob.goto(600, -60)
    bob.pendown()
    bob.begin_fill()
    bob.goto(-600, -280)
    bob.goto(600, -280)
    bob.goto(600, -60)
    bob.end_fill()
    bob.penup()
    bob.color("green", "#4f5d40")
    bob.goto(-600, -140)
    bob.pendown()
    bob.begin_fill()
    bob.goto(-600, -325)
    bob.goto(350, -325)
    bob.goto(-600, -140)
    bob.penup()
    bob.end_fill()
    bob.color("#112619", "#6d6a3f")
    bob.goto(-600, -275)
    bob.begin_fill()
    bob.pendown()
    bob.goto(600, -200)
    bob.goto(600, -325)
    bob.goto(-600, -325)
    bob.goto(-600, -275)
    bob.end_fill()
    bob.penup()
    draw_cloud(bob, 15, [300, 250])
    draw_cloud(bob, 12, [-400, 300])
    draw_tree(bob, 2.3, [-500, -210], "#292b1b")
    draw_tree(bob, 1.8, [-510, -215], "#296211")
    draw_tree(bob, 3, [-550, -250], "dark green")
    draw_tree(bob, 1, [550, -55], "#296211")
    draw_tree(bob, 0.9, [490, -75], "#292b1b")


def draw_line(turt: Turtle, start_pos: list[int], end_pos: list[int]) -> None:
    """Function that draws a line between two points - returns None."""
    turt.penup()
    turt.goto(start_pos[0], start_pos[1])
    turt.pendown()
    turt.goto(end_pos[0], end_pos[1])


def draw_rect(turt: Turtle, top_left: list[int], bottom_right: list[int]) -> None:
    """Function that draws and fills a rectangle when given the coordenates of the top-left corner and the bottom-right corner - returns none."""
    turt.penup()
    turt.goto(top_left[0], top_left[1])
    turt.pendown()
    turt.begin_fill()
    turt.setheading(0)
    rect_width: int = abs(top_left[0] - bottom_right[0])
    rect_height: int = abs(top_left[1] - bottom_right[1])
    i: int = 0
    while i < 2:
        turt.forward(rect_width)
        turt.right(90)
        turt.forward(rect_height)
        turt.right(90)
        i += 1
    turt.end_fill()


def draw_triangle(turt: Turtle, size: float) -> None:
    """Function that draws a triangle when given an input of a Turtle object and a size float - returns None."""
    turt.setheading(0)
    turt.forward(20 * size)
    turt.left(120)
    i: int = 0
    while i < 2:
        turt.forward(40 * size)
        turt.left(120)
        i += 1
    turt.forward(20 * size)


def draw_mount(turt: Turtle, bottom_left: list[int], bottom_right: list[int], peak_pos: list[int]) -> None:
    """Function that will draw a mountain given a Turtle object and three points - returns None."""
    turt.penup()
    turt.color("grey", "dark grey")
    turt.goto(bottom_left[0], bottom_left[1])
    turt.pendown()
    turt.begin_fill()
    turt.goto(peak_pos[0], peak_pos[1])
    turt.goto(bottom_right[1], bottom_right[1])
    turt.goto(bottom_left[0], bottom_left[1])
    turt.penup()
    turt.end_fill()


def draw_and_fill_circle(turt: Turtle, rad: float) -> None:
    """Helper function that draws and fills a circle - returns None."""
    turt.pendown()
    turt.begin_fill()
    turt.circle(rad)
    turt.penup()
    turt.end_fill()


def draw_cloud(turt: Turtle, size: float, pos: list[int]) -> None:
    """Function that will draw a cloud given a Turtle object, a size float, and a position - returns None."""
    turt.color("light grey")
    turt.penup()
    i: int = 0
    x: int = 0
    y: int = 0
    while i < 20:
        x = random.randint(pos[0] - 100, pos[0] + 100)
        y = random.randint(pos[1] - 60, pos[1] + 60)
        turt.goto(x, y)
        draw_and_fill_circle(turt, size)
        i += 1


def draw_tree(turt: Turtle, size: float, trunk_position: list[float], hex_code: str) -> None:
    """Function that draws a treeof specified color and size when given an input of a Turtle object, float for size, coordenate for the trunk, and a hex code for color - returns none."""
    turt.color(hex_code, hex_code)
    turt.setposition(trunk_position[0], trunk_position[1])
    i: int = 1
    while i <= 7:
        turt.pendown()
        turt.begin_fill()
        draw_triangle(turt, size)
        turt.penup()
        turt.end_fill()
        turt.setposition(trunk_position[0], (trunk_position[1] + (size * 10 * i)))
        turt.pendown()
        turt.begin_fill()
        draw_triangle(turt, 0.75 * size)
        turt.penup()
        turt.end_fill()
        turt.setposition(trunk_position[0], (trunk_position[1] + (size * 10 * i)))
        i += 1


if __name__ == '__main__':
    main()
    done()