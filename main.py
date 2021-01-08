from turtle import Screen, Turtle
from players import Player
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

player = Player()

screen.onkey(key="Up", fun=player.up)
screen.onkey(key="Down", fun=player.down)

screen.listen()

line = Turtle()
line.color("white")
line.width(10)
line.penup()
line.goto(0, -400)
line.pendown()
line.setheading(90)
for i in range(17):
    line.forward(30)
    line.penup()
    line.forward(20)
    line.pendown()

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.02)
    ball.move()

    if ball.xcor() < player.segments[0].xcor() + 20:
        if player.segments[0].ycor() - 20 < ball.ycor() < player.segments[3].ycor() + 20:
            ball.setheading(180 - ball.heading() + 20)

    if ball.xcor() > player.segments_cpu[0].xcor() - 20:
        if player.segments_cpu[0].ycor() - 20 < ball.ycor() < player.segments_cpu[3].ycor() + 20:
            ball.setheading(180 - ball.heading() + 20)

    if ball.xcor() > 420:
        scoreboard.increase_score_1()
        ball.refresh()
    elif ball.xcor() < -420:
        scoreboard.increase_score_2()
        ball.refresh()

    if ball.ycor() > player.segments_cpu[3].ycor() and ball.xcor() > 0:
        player.cpu_up()
    elif ball.ycor() < player.segments_cpu[0].ycor() and ball.xcor() > 0:
        player.cpu_down()

    if scoreboard.score1 == 5 or scoreboard.score2 == 5:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
