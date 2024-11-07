from turtle import *

setup(650, 350, 200, 200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("red")
seth(-30)
for i in range(6):
    circle(30, 80)
    circle(-30, 80)
circle(30, 80 / 2)
fd(30)
circle(16, 180)
fd(30 * 2 / 3)
