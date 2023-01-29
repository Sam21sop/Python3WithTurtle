import turtle
t = turtle.Turtle()

t.speed(0)
t.screen.bgcolor('black')

colors = ['red', 'green', 'pink', 'yellow']
for x in range(300):
    t.color(colors[x%4])
    t.forward(x)
    t.left(90)