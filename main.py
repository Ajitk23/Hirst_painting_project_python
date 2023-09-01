from scr import color_list
import turtle as T
import random


T.colormode(255)
ak = T.Turtle()
ak.speed("fastest")
ak.penup()
ak.hideturtle()

ak.setheading(220)
ak.forward(300)
ak.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    ak.dot(20, random.choice(color_list))
    ak.forward(50)
    
    if dot_count%10 == 0:
        ak.setheading(90)
        ak.forward(50)
        ak.setheading(180)
        ak.forward(500)
        ak.setheading(0)


screen = T.Screen()
screen.exitonclick()