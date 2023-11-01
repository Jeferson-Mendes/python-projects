from turtle import Turtle
from food import SCREEN_WIDTH, SCREEN_HEIGHT

TURTLE_SIZE = 20
STARTING_X_COORDINATE = 0
STARTING_Y_COORDINATE = 0
COLLISION_THRESHOLD = 5


def create_snake_segment():
    seg = Turtle(shape='square')
    seg.color('white')
    seg.penup()
    return seg


class Snake:
    head: Turtle

    def __init__(self, screen, length=3):
        self.screen = screen
        self.snake = None
        self.len = length
        self.init_snake()
        self.game_status = True
        self.head = self.snake[0]  # Using the first turtle object of the snake to detect collisions, navigate, etc
        # Hence, kept as separate attribute

    def init_snake(self):
        self.snake = []
        for i in range(self.len):
            seg = create_snake_segment()
            seg.setpos(STARTING_X_COORDINATE - i * TURTLE_SIZE, STARTING_Y_COORDINATE)  # 20 is the size of the turtle
            self.snake.append(seg)

    def collision(self):
        for turt in self.snake[1:]:
            if turt.pos() == self.head.pos():
                return True
        return False

    def game_over(self):
        if self.collision():
            return True
        elif abs(abs(self.head.pos()[0]) - (SCREEN_WIDTH / 2)) < COLLISION_THRESHOLD:
            return True
        elif abs(abs(self.head.pos()[1]) - (SCREEN_HEIGHT / 2)) < COLLISION_THRESHOLD:
            return True
        else:
            return False

    def extend_snake(self):
        seg = create_snake_segment()
        prev_turt = self.snake[-1]
        heading = prev_turt.heading()
        pos = prev_turt.pos()
        seg.setheading(heading)
        if heading == 270:
            seg.setpos(pos[0], pos[1] + TURTLE_SIZE)
        if heading == 90:
            seg.setpos(pos[0], pos[1] - TURTLE_SIZE)
        if heading == 0:
            seg.setpos(pos[0] - TURTLE_SIZE, pos[1])
        if heading == 180:
            seg.setpos(pos[0] + TURTLE_SIZE, pos[1])
        self.snake.append(seg)

    def snake_body_move(self, new_heading):
        old_pos = self.head.pos()
        self.head.setheading(new_heading)
        self.head.forward(TURTLE_SIZE)
        for s in range(1, len(self.snake)):
            self.snake[s].setposition(old_pos[0], old_pos[1])
            self.snake[s].setheading(new_heading)

    def godown(self):
        if self.head.heading() != 90:  # Cannot go down if the snake is moving up
            self.snake_body_move(-90)

    def goright(self):
        if self.head.heading() != 180:  # Cannot go right if the snake is moving left
            self.snake_body_move(0)

    def goup(self):
        if self.head.heading() != 270:  # Cannot go up if the snake is moving down
            self.snake_body_move(90)

    def goleft(self):
        if self.head.heading() != 0:  # Cannot go left if the snake is moving right
            self.snake_body_move(180)

    def goforward(self):
        for turt in self.snake:
            turt.forward(20)

    def halted(self):
        print('Stopping')
        self.game_status = False

    def move(self):
        if self.screen.onkey(self.godown, 's'):
            return self.game_status
        elif self.screen.onkey(self.goup, 'w'):
            return self.game_status
        elif self.screen.onkey(self.goleft, 'a'):
            return self.game_status
        elif self.screen.onkey(self.goright, 'd'):
            return self.game_status
        elif self.screen.onkey(self.halted, 'q'):
            return self.game_status
        else:
            self.goforward()
            return self.game_status
