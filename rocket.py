import turtle


class Rocket:
    def __init__(self, x, y, width=10, height=50):
        self.__pen = turtle.Turtle()
        self.width = width
        self.height = height
        self.__pen.goto(x, y)
        self.__pen.speed(0)

    def init_rocket(self):
        pen = self.__pen
        pen.color('white')
        pen.shape('square')
        pen.shapesize(stretch_len=self.width / 10, stretch_wid=self.height / 10)
        pen.penup()

    @property
    def x(self):
        return self.__pen.xcor()

    @property
    def y(self):
        return self.__pen.ycor()

    @y.setter
    def y(self, y):
        self.__pen.sety(y)
