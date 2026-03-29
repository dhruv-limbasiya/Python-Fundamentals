from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwords():
    tim.forward(10)


def move_backwords():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_the_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forwords, key="w")
screen.onkey(fun=move_backwords, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear_the_screen, key="c")
screen.exitonclick()
