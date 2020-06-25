import turtle
from collections import namedtuple

Pos = namedtuple('Pos', 'x y')
Speed = namedtuple('Speed', 'dx dy')


class Ball:
    def __init__(self):
        self.__pen = turtle.Turtle()
        self.__pen.speed(0)
        self.dx = 0
        self.dy = 0

    def init_ball(self):
        pen = self.__pen
        pen.penup()
        pen.color('red')
        pen.shape('circle')

    @property
    def x(self):
        return self.__pen.xcor()

    @x.setter
    def x(self, x):
        self.__pen.setx(x)

    @property
    def y(self):
        return self.__pen.ycor()

    @y.setter
    def y(self, y):
        self.__pen.sety(y)

    @property
    def radius(self):
        return 10
