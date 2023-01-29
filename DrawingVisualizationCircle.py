import turtle
import time

t = turtle.Turtle()

t.color('red')
for angle in range(0, 360, 10):
    t.seth(angle)
    t.circle(100)
    time.sleep(1)