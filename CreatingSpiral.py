import turtle
import random as r

t = turtle.Turtle()

t.speed(0)
t.screen.bgcolor('black')

colors = ['red', 'yellow', 'pink', 'orange', 'blue', 'green', 'cyan', 'white']

for x in range (300):
    t.color(colors[x%6])
    t.forward(x)
    t.left(59)