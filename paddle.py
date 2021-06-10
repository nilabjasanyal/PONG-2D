from turtle import Turtle


class PaddleClass(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("magenta")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(x,y)
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)




