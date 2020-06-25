# class Rect:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @property
#     def height(self):
#         return self.__height
#
#     @property
#     def left_top(self):
#         return -self.__width / 2, self.__height / 2
#
#     @property
#     def left_bottom(self):
#         return -self.__width / 2, -self.__height / 2
#
#     @property
#     def right_top(self):
#         return self.__width / 2, self.__height / 2
#
#     @property
#     def right_bottom(self):
#         return self.__width / 2, -self.__height / 2
#
#     @property
#     def top_middle(self):
#         return 0, self.__height / 2
#
#     @property
#     def bottom_middle(self):
#         return 0, -self.__height / 2
