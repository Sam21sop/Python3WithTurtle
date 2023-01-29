import turtle
import time

t = turtle.Turtle()

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)


if __name__ == "__main__":
    square(150)
    time.sleep(10)