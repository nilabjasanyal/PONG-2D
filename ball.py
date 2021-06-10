from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('rosy brown')
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.angle=50
        self.setheading(self.angle)
        self.x_move=10
        self.y_move=10
        # self.speed('slowest')
        # game_on=True
        # self.forward(5)
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
        # self.forward(0.1)

    def bounce_on_wall(self):
        self.y_move*=-1

    def bounce_on_paddle(self):
        self.x_move*=-1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_on_paddle()