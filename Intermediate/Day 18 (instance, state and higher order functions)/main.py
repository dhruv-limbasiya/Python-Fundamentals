from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)  # this function allows to set height and width
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color from 'red, orange, yellow, green ,blue, purple': ")  # this function take inpuut through a new pop up window in string
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True
else:
    print("You didn't bet.")

while is_race_on:
    for turtle in all_turtle:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

screen.exitonclick()
