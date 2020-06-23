import turtle


class Rocket:
    def __init__(self, x, y, width=1, height=5):
        self.__pen = turtle.Turtle()
        self.__width = width
        self.__height = height
        self.__pen.goto(x, y)
        self.__pen.speed(0)

    def init_rocket(self):
        pen = self.__pen
        pen.color('white')
        pen.shape('square')
        pen.shapesize(stretch_len=self.__width, stretch_wid=self.__height)
        pen.penup()

    @property
    def y(self):
        return self.__pen.ycor()

    @y.setter
    def y(self, y):
        self.__pen.sety(y)

    @property
    def height_px(self):
        return self.__height * 10
