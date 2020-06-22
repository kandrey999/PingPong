class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.left_top = (-width / 2, height / 2)
        self.left_bottom = (-width / 2, -height / 2)
        self.right_top = (width / 2, height / 2)
        self.right_bottom = (width / 2, -height / 2)
        self.top_middle = (0, height / 2)
        self.bottom_middle = (0, -height / 2)
