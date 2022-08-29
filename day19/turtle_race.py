
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle  will win the race? enter colour:")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:


    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! The {winning_color} turtle won the race")
            else:
                print(f"you've lose! The {winning_color} turtle won the race")

        random_distant = random.randint(0, 10)
        turtle.forward(random_distant)

screen.exitonclick()
