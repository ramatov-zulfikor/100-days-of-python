from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.sety(new_y)
