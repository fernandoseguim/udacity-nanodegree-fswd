import turtle


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
    color = ['blue', 'red', 'green', 'purple', 'cyan', 'pink', 'black', 'yellow', 'brown', 'orange']
    brad.speed(100)
    count = 0
    distance = 100

    while True:

        brad.color("purple")
        if count > 36:
            distance = distance * 1.2
            count = 0

        for i in range(0, 4):
            walk(brad, distance=distance)
        brad.right(10)
        count += 1


if __name__ == '__main__':
    window = turtle.Screen()
    draw_square()
    window.exitonclick()