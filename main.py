import another_module
print(another_module.another_variable)

import turtle
timmy=turtle.Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
i=1
while(i<=4):
    timmy.forward(100)
    timmy.left(90)
    i+=1
    timmy.speed(0.3)


screen=turtle.Screen()
print(screen.canvheight,"X",screen.canvwidth)
screen.exitonclick()
