#importing Turtle and Screen.
from turtle import Turtle,Screen

#creating timmy and screen objects
timmy = Turtle()
screen = Screen()

#differnt functions to perform desired moves by turtle.
def moveForward():
    timmy.forward(25)

def moveBackwards():
    timmy.backward(25) 

def moveClockwise():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def moveCounterclockwise():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clearScreen():
    timmy.clear()
    timmy.reset()

screen.listen()
#Asking keys to listen the user by assigning different keys to different functions.
screen.onkey(key="w",fun=moveForward)
screen.onkey(key="s",fun=moveBackwards)
screen.onkey(key="a",fun=moveCounterclockwise)
screen.onkey(key="d",fun=moveClockwise)
screen.onkey(key="c",fun=clearScreen)

screen.exitonclick()
