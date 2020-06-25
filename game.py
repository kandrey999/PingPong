import turtle
from rocket import Rocket
from ball import Ball
from random import randint, choice
from score import Score
from gamearea import GameArea


class Game:
    def __init__(self, width, height, step=40):
        self.__window = turtle.Screen()
        self.__window.setup(width=width, height=height)
        self.__area = GameArea(width, height)
        self.__ball = Ball()
        self.__left_rocket = Rocket(-width / 2 + width / 10, 0)
        self.__right_rocket = Rocket(width / 2 - width / 10, 0)
        self.__left_score = Score((self.__area.border.left, self.__area.border.top), ('Arial', self.__area.width // 12))
        self.__right_score = Score((self.__area.border.right, self.__area.border.top),
                                   ('Arial', self.__area.width // 12))
        self.__speeds = [-5, -4, -3, 3, 4, 5]
        self.__step = step

    def __init_game(self):
        self.__window.bgcolor('black')
        self.__area.init_area()
        self.__left_rocket.init_rocket()
        self.__right_rocket.init_rocket()
        self.__ball.init_ball()
        self.__left_score.init_score()
        self.__right_score.init_score()

    def __move_ball(self):
        ball = self.__ball
        self.__set_random_ball_speed()
        while True:
            ball.x = ball.x + ball.dx
            ball.y = ball.y + ball.dy

            if self.__detect_collision_top_bottom_wall():
                self.__reverse_ball_direction_y()

            if self.__detect_collision_left_rocket() or self.__detect_collision_right_rocket():  # ПРОБЛЕМА С ПРОВЕРКОЙ СТОЛКНОВЕНИЯ С РАКЕТКАМИ, ШАР РАЗВОРАЧИВАЕТ ОШИБОЧНО.
                self.__reverse_ball_direction_x()

            # if self.__detect_collision_left_right_wall():
            #     self.__set_random_ball_speed()
            #     self.__reset_ball_position()
            if self.__detect_collision_left_wall():
                self.__set_random_ball_speed()
                self.__reset_ball_position()
                self.__right_score.change_and_write_score()

            if self.__detect_collision_right_wall():
                self.__set_random_ball_speed()
                self.__reset_ball_position()
                self.__left_score.change_and_write_score()

    def __detect_collision_right_wall(self):
        return self.__ball.x >= self.__area.border.right - self.__ball.radius

    def __detect_collision_left_wall(self):
        return self.__ball.x <= self.__area.border.left + self.__ball.radius

    def __detect_collision_top_bottom_wall(self):
        return self.__ball.y >= self.__area.border.top - self.__ball.radius \
               or self.__ball.y <= - self.__area.border.top + self.__ball.radius

    def __detect_collision_left_rocket(self):
        ball = self.__ball
        rocket = self.__left_rocket
        left_rocket_collision_x = rocket.x + ball.radius + rocket.width / 2
        left_rocket_top_collision_y = rocket.y + rocket.height / 2 + ball.radius
        left_rocket_bottom_collision_y = rocket.y - rocket.height / 2 - ball.radius

        return ball.x == left_rocket_collision_x \
               and left_rocket_bottom_collision_y <= self.__ball.y <= left_rocket_top_collision_y

    def __detect_collision_right_rocket(self):
        ball = self.__ball
        rocket = self.__right_rocket
        right_rocket_collision_x = rocket.x - ball.radius - rocket.width / 2
        right_rocket_top_collision_y = rocket.y + rocket.height / 2 + ball.radius
        right_rocket_bottom_collision_y = rocket.y - rocket.height / 2 - ball.radius

        return ball.x == right_rocket_collision_x \
               and right_rocket_bottom_collision_y <= ball.y <= right_rocket_top_collision_y

    def __set_random_ball_speed(self):
        self.__ball.dx = choice(self.__speeds)
        self.__ball.dy = choice(self.__speeds)

    def __reverse_ball_direction_y(self):
        self.__ball.dy = -1 * self.__ball.dy

    def __reverse_ball_direction_x(self):
        self.__ball.dx = -1 * self.__ball.dx

    def __reset_ball_position(self):
        self.__ball.x = 0
        self.__ball.y = randint(self.__area.border.bottom, self.__area.border.top)

    def __left_rocket_up(self):
        y = min(self.__area.height / 2 - self.__left_rocket.height,
                self.__left_rocket.y + self.__step)
        self.__left_rocket.y = y

    def __left_rocket_down(self):
        y = max(-self.__area.height / 2 + self.__left_rocket.height,
                self.__left_rocket.y - self.__step)
        self.__left_rocket.y = y

    def __right_rocket_up(self):
        y = min(self.__area.height / 2 - self.__right_rocket.height,
                self.__right_rocket.y + self.__step)
        self.__right_rocket.y = y

    def __right_rocket_down(self):
        y = max(-self.__area.height / 2 + self.__right_rocket.height,
                self.__right_rocket.y - self.__step)
        self.__right_rocket.y = y

    def run(self):
        self.__init_game()

        self.__window.listen()
        self.__window.onkeypress(self.__left_rocket_up, 'w')
        self.__window.onkeypress(self.__left_rocket_down, 's')
        self.__window.onkeypress(self.__right_rocket_up, 'Up')
        self.__window.onkeypress(self.__right_rocket_down, 'Down')
        self.__move_ball()
        self.__window.mainloop()
