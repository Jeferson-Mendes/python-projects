from turtle import Turtle
from food import SCREEN_WIDTH, SCREEN_HEIGHT

TIME_SCORE = 1
FEED_SCORE = 15
SCORE_DISPLAY_OFFSET_Y = 30  # Offset of score display from top of the game window
SCORE_DISPLAY_OFFSET_X = SCREEN_WIDTH / 2  # Offset of score display from top of the game window


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.time_score = TIME_SCORE
        self.feed_score = FEED_SCORE
        self.score = 0
        self.color('white')
        self.penup()
        self.setpos(int(SCREEN_HEIGHT / 2) - SCORE_DISPLAY_OFFSET_X, int(SCREEN_HEIGHT / 2) - SCORE_DISPLAY_OFFSET_Y)
        self.hideturtle()
        self.high_score = 0

    def display_score(self,high_score):
        super().clear()
        if high_score < self.score:
            high_score = self.score
        super().write('SCORE: ' + str(self.score) + '\t\t\t' + 'HIGH SCORE: ' + str(high_score), align='center',
                      font=('Arial', 12, 'normal'))
        return high_score

    def display_game_over(self):
        self.home()
        super().write('GAME OVER', align='center',
                      font=('Courier', 18, 'normal'))
