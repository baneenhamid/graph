import turtle
r=turtle.Turtle()
r.speed(0)
r.getscreen().bgcolor("black")
for i in range(5):
    for colours in["red","blue","magenta","cyan","green","yellow","white"]:
        r.color(colours)
        r.pensize(3)
        r.left(12)
        r.forward(200)
        r.left(90)
        r.forward(200)
        r.left(90)
        r.forward(200)
        r.left(90)
        r.forward(200)
        r.left(90)


turtle.done()


