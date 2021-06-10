import turtle as t
from paddle import PaddleClass
from ball import Ball
import time
from scoreboard import ScoreBoard

score=0
my_screen=t.Screen()
my_screen.setup(width=900,height=600)
my_screen.bgcolor('aquamarine')
my_screen.tracer(0)

pong=Ball()
left_paddle=PaddleClass(-430,0)
right_paddle=PaddleClass(430,0)
my_screen.listen()
my_screen.onkey(left_paddle.up,"w")
my_screen.onkey(left_paddle.down,"s")
my_screen.onkey(right_paddle.up,'Up')
my_screen.onkey(right_paddle.down,'Down')

should_continue=True
point_board=ScoreBoard()

while should_continue:
    time.sleep(0.035)
    my_screen.update()
    pong.move()
    if pong.ycor() >= 280 or pong.ycor() <=-280:
        pong.bounce_on_wall()
    if (pong.distance(left_paddle)<50 and pong.xcor() < -400) or (pong.distance(right_paddle)<30 and pong.xcor()>400) :
        pong.bounce_on_paddle()
        score+=1
    if pong.xcor()>440 :
        # should_continue=False
        # point_board.game_over()
        pong.reset_position()
        point_board.l_point()

    if  pong.xcor() <-440:
        pong.reset_position()
        point_board.r_point()

my_screen.exitonclick()