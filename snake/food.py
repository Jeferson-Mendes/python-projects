from turtle import Turtle
import random

STAY_PRESENT = 20
FEED_SCORE = 5
APPEAR_TRIGGER = 10
BORDER = 10
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Food(Turtle):
    def __init__(self, screen_wide=SCREEN_WIDTH, screen_high=SCREEN_HEIGHT):
        super().__init__()
        self.presence = None  # if the food is present on the screen or not
        self.screen_width, self.screen_height = screen_wide, screen_high
        self.shape('circle')
        self.color('white')
        self.penup()
        self.time_present = STAY_PRESENT
        self.x = random.randint(int(-self.screen_width / 2) + BORDER, int(self.screen_height / 2) - BORDER)
        self.y = random.randint(int(-self.screen_width / 2) + BORDER, int(self.screen_height / 2) - BORDER)
        self.setpos(self.x, self.y)
