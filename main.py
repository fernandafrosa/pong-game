#Pong game
#Fernanda

#steps:
# - create the screen
# - create and move paddle
# - create another paddle
# - create the ball and make it move
# - detect collision with wall and bouce
# - detect collision with paddle
# - detect when paddle misses
# - keep score

#TODO: importing libraries
from turtle import Screen
import time

#TODO: create the screen
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor('black')
screen.title("Fernanda´s Pong Game")
screen.tracer(0)


screen.exitonclick()