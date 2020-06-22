import turtle
from rect import Rect


class Game:
    def __init__(self, width, height):
        self.window = turtle.Screen()
        self.window.setup(width=width, height=height)
        self.pen = turtle.Turtle()
        self.area = Rect(width, height)

    def __init_area(self):
        pen = self.pen
        area = self.area
        pen.color('green')
        self.window.bgcolor('black')
        pen.begin_fill()
        pen.goto(area.left_top)
        pen.goto(area.right_top)
        pen.goto(area.right_bottom)
        pen.goto(area.left_bottom)
        pen.goto(area.left_top)
        pen.end_fill()
        pen.goto(area.top_middle)
        pen.setheading(270)
        strip_count = int(area.height / 25)
        strip_len = area.height / strip_count
        pen.color('white')
        for i in range(strip_count):
            if i % 2 == 0:
                pen.forward(strip_len)
            else:
                pen.penup()
                pen.forward(strip_len)
                pen.pendown()

        pen.hideturtle()

    def run(self):
        self.__init_area()
        self.window.mainloop()
