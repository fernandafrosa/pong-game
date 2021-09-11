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

#TODO: create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Fernanda´s Pong Game")
screen.tracer(0)



#TODO: CREATE PADDLE:

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_on = True
while game_on:
    screen.update()

screen.exitonclick()