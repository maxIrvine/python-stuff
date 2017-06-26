from turtle import *
import colorsys

turtle = Turtle()
turtle2 = Turtle()

# def center_turtle():
#     up()
#     left(90)
#     forward(50)
#     down()

# def center_star():
#     up()
#     left(45)
#     forward(20)
#     right(50)
#     down()

# def draw_circle(w, size, outerColor, innerColor):
#     begin_fill()
#     fillcolor(innerColor)
#     pencolor(outerColor)
#     width(w)
#     circle(size)
#     end_fill()

# def star(size, outerColor):
#     pencolor(outerColor)
#     for i in range(5):
#         forward(size)
#         right(144)

# def rainbowMadness():
#     for i in range(1000):
#         color = colorsys.hsv_to_rgb(i/1000, 1.0, 1.0)
#         color[color]
#         forward(i)
#         right(98)

def sun():
    # color('red', 'yellow')
    colormode(255)
    # begin_fill()
    width(1)
    count = 0
    i = 1
    j = 1
    while True and count <= 200:
        if (count < 100):
            c = i, 172, 247
            i = i + 2
        else:
            c = 220, j, 247
            j = j + 2
        turtle.pencolor(c)
        turtle.forward(500)
        turtle.left(170)
        turtle.forward(250)
        turtle.left(172)
        turtle.forward(250)
        turtle.left(172)
        print count
        count = count + 1
        if abs(pos()) < 1:
            break
    # end_fill()

def bonkers():
    # begin_fill()
    colormode(255)
    count = 0
    i = 1
    j = 1
    while count < 140:
        if (count < 100):
            c = i, 172, 247
            i = i + 2
        else:
            c = 220, j, 247
            j = j + 2
        turtle.pencolor(c)
        turtle.forward(300)
        turtle.left(170)
        turtle.draw_circle(1, 5, c, c)
        turtle.forward(150)
        turtle.left(60)
        turtle.forward(30)
        turtle.right(75)
        turtle.forward(151)
        count = count + 1
        print count
    # end_fill()
def main():
    #draws a circle with a star in it
    # def circle_star():
    #     draw_circle(10, 100, "blue", "green")
    #     center_turtle()
    #     center_star()
    #     star(75, "orange")
    
    # circle_star()
    # right(270)
    # forward(200)
    # circle_star()
    # rainbowMadness()
    turtle.speed(10)
    turtle2.speed
    up()
    left(270)
    forward(1)
    left(180)
    down()
    speed(10)
    sun()
    bonkers()
    mainloop()

main()