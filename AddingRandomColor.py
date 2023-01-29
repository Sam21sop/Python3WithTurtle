import turtle
import random
t = turtle.Turtle()
t.screen.bgcolor('black')
t.speed(0)

#colors = ['red', 'yellow', 'pink', 'orange'] #previous color set
colors = ['red', 'yellow', 'pink', 'orange', 'blue', 'green', 'cyan', 'white']

for x in range(600):
    t.color(colors[random.randint(0, 7)])
    t.forward(x)
    t.left(90)