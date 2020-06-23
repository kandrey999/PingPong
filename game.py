import turtle
from rect import Rect
from rocket import Rocket


class Game:
    def __init__(self, width, height):
        self.window = turtle.Screen()
        self.width = width
        self.window.setup(width=width, height=height)
        self.pen = turtle.Turtle()
        self.area = Rect(width, height)
        self.left_rocket = Rocket(-width / 2 + width / 10, 0)
        self.right_rocket = Rocket(width / 2 - width / 10, 0)
        self.step = 40

    def __init_area(self):
        pen = self.pen
        area = self.area
        pen.speed(0)
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

    def init_rockets(self):
        self.left_rocket.init_rocket()
        self.right_rocket.init_rocket()

    def left_rocket_up(self):
        y = min(self.area.height / 2 - self.left_rocket.height_px,
                self.left_rocket.y + self.step)
        self.left_rocket.y = y

    def left_rocket_down(self):
        y = max(-self.area.height / 2 + self.left_rocket.height_px,
                self.left_rocket.y - self.step)
        self.left_rocket.y = y

    def right_rocket_up(self):
        y = min(self.area.height / 2 - self.right_rocket.height_px,
                self.right_rocket.y + self.step)
        self.right_rocket.y = y

    def right_rocket_down(self):
        y = max(-self.area.height / 2 + self.right_rocket.height_px,
                self.right_rocket.y - self.step)
        self.right_rocket.y = y

    def run(self):
        self.__init_area()
        self.init_rockets()
        self.window.listen()
        self.window.onkeypress(self.left_rocket_up, 'w')
        self.window.onkeypress(self.left_rocket_down, 's')
        self.window.onkeypress(self.right_rocket_up, 'Up')
        self.window.onkeypress(self.right_rocket_down, 'Down')
        self.window.mainloop()
