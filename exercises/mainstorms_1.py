import turtle, _thread


def walk(t, front=True, distance=100, rotate="right", angle=90):
    if front:
        t.forward(distance)
    else:
        t.backward(distance)

    if rotate == "right":
        t.right(angle)

    if rotate == "left":
        t.left(angle)


def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("purple")

    while True:
        for i in range(0, 4):
            walk(brad)


def draw_circle():
    angle = turtle.Turtle()
    angle.shape("arrow")
    angle.color("green")
    while True:
        angle.circle(75)


def draw_triangle():
    fred = turtle.Turtle()
    fred.shape("arrow")
    fred.color("yellow")

    while True:
        walk(fred, False, 150, rotate="right", angle=60)
        walk(fred, True, 150, rotate="left", angle=120)
        walk(fred, True, 150, rotate="right", angle=60)


def start():
    window = turtle.Screen()
    window.bgcolor("cyan")
    _thread.start_new_thread(draw_square, ())
    _thread.start_new_thread(draw_circle, ())
    _thread.start_new_thread(draw_triangle, ())
    window.exitonclick()


if __name__ == '__main__':
    start()
