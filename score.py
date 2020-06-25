import turtle


class Score:
    def __init__(self, coordinates, font):
        self.__count = 0
        self.__coordinates = coordinates
        self.__font = font
        self.__pen = turtle.Turtle()

    def init_score(self):
        self.__pen.goto(*self.__coordinates)
        self.__pen.hideturtle()
        self.__pen.color('white')
        self.__pen.write(self.__count, font=self.__font)

    def change_and_write_score(self):
        self.__count += 1
        self.__pen.clear()
        self.__pen.write(self.__count, font=self.__font)
