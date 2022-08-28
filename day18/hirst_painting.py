import turtle as turtle_module
import random

turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colour_list = [(206, 161, 82), (55, 88, 129), (142, 91, 41), (221, 207, 107), (138, 26, 48), (133, 175, 200), (157, 47, 84), (46, 55, 102), (169, 159, 41), (131, 188, 145), (82, 20, 43), (36, 43, 68), (186, 93, 106), (189, 139, 163), (87, 115, 177), (87, 156, 97), (59, 39, 33), (79, 154, 165), (196, 81, 71), (54, 128, 122), (45, 73, 76), (162, 202, 216), (44, 75, 73), (78, 76, 45), (167, 207, 165), (219, 175, 187)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)


number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if dot_count%10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
