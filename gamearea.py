import turtle
from collections import namedtuple

Border = namedtuple('Border', 'left top right bottom')


class GameArea:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__border = Border(-width / 2, height / 2, width / 2, -height / 2)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def left_top(self):
        return -self.__width / 2, self.__height / 2

    @property
    def left_bottom(self):
        return -self.__width / 2, -self.__height / 2

    @property
    def right_top(self):
        return self.__width / 2, self.__height / 2

    @property
    def right_bottom(self):
        return self.__width / 2, -self.__height / 2

    @property
    def top_middle(self):
        return 0, self.__height / 2

    @property
    def bottom_middle(self):
        return 0, -self.__height / 2

    @property
    def border(self):
        return self.__border

    def init_area(self):
        pen = turtle.Turtle()
        # area = self.area
        pen.speed(0)
        pen.color('green')
        # self.window.bgcolor('black')
        pen.begin_fill()
        pen.goto(self.left_top)
        pen.goto(self.right_top)
        pen.goto(self.right_bottom)
        pen.goto(self.left_bottom)
        pen.goto(self.left_top)
        pen.end_fill()
        pen.goto(self.top_middle)
        pen.setheading(270)
        strip_count = int(self.height / 25)
        strip_len = self.height / strip_count
        pen.color('white')
        for i in range(strip_count):
            if i % 2 == 0:
                pen.forward(strip_len)
            else:
                pen.penup()
                pen.forward(strip_len)
                pen.pendown()

        pen.hideturtle()
