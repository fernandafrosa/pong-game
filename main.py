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
from paddle import Paddle
from ball import Ball
import time

#TODO: create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Fernanda´s Pong Game")
screen.tracer(0)



#TODO: CREATE PADDLE and ball :

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #TODO: Detect ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #TODO: Detect ball collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()


screen.exitonclick()