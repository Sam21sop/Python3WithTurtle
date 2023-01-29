import turtle
import time
import random

t = turtle.Turtle()

#t.speed(10)

t.screen.bgcolor('black')
turns = 100
distance = 10

for x in range(turns):
    right = t.right(random.randint(0, 360))
    left = t.left(random.randint(0, 360))
    t.color(random.choice(['Blue', 'Red', 'Green']))
    random.choice([right, left])
    t.forward(distance)