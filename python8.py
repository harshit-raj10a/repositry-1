from turtle import *
import random
for i in range(50):
    penup()
    goto(random.randint(-40,40),random.randint(-400,400))
    pendown()
    red_amount=random.randint(0,3)/100.0
    blue_amount=random.randint(0,3)/100.0
    green_amount=random.randint(0,3)/100.0
    pencolor((red_amount,blue_amount,green_amount))
    circle_size=random.randint(10,40)
    pensize(random.randint(4,6))

    for i in range(6):
        circle(circle_size)
        left(60)
