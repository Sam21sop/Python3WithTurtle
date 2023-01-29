import turtle

t = turtle.Turtle()
t.screen.bgcolor('black')
t.speed(0)

#colors = ['red', 'yellow', 'pink', 'orange'] #previous color set
colors = ['red', 'yellow', 'pink', 'orange', 'blue', 'green', 'cyan', 'white']

for x in range(500):
    t.color(colors[x%8])
    t.forward(x)
    t.left(90)
