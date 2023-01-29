import turtle

t = turtle.Turtle()

t.speed(0)
t.screen.bgcolor('black')
colors = ['red', 'orange', 'yellow', 'pink']
while True:
    for x in range(100):
        t.circle(x)
        t.color(colors[x % 4])
        t.left(60)